#! /usr/bin/env python

from __future__ import print_function

import os
import sys
import yaml
import jinja2
import argparse
import importlib

from exceptions import AttributeError

# List of supported docker-compose commands
OPTIONS_CAPABILITIES = [
    "cap_add",
    "cap_drop",
    "command",
    "container_name",
    "cpu_shares",
    "cpuset",
    "devices",
    "domainname",
    "dns",
    "dns_search",
    "entrypoint",
    "env_file",
    "environment",
    "expose",
    "hostname",
    "links",
    "log_driver",
    "mac_address",
    "mem_limit",
    "memswap_limit",
    "net",
    "pid",
    "ports",
    "privileged",
    "read_only",
    "restart",
    "stdin_open",
    "tty",
    "user",
    "volume_driver",
    "volumes",
    "volumes_from",
    "working_dir",
]

# Setup cli handler
parser = argparse.ArgumentParser(description="Translate docker-compose templates to process manage service files " \
    "(systemd currently supported).")

parser.add_argument(
    ['-f', '--file'],
    required=True,
    help='Specify docker-compose files (default: docker-compose.yml)',
    default='docker-compose.yml',
    dest='files',
    action='append',
)

# Get cli arguments
args = parser.parse_args()


def underscore_to_camelcase(value):
    def upperfirst(x):
        return x[0].upper() + x[1:]
    def camelcase():
        yield str.lower
        while True:
            yield str.capitalize
    c = camelcase()
    return upperfirst("".join(c.next()(x) if x else '_' for x in value.split("_")))


docker_services = {}

# Loop through given files
for file in args.files:

    # Load YAML into python
    with open(file, 'r') as stream:
        services_set = yaml.parse(stream)

    # Loop through services from YAML file
    for service_name, service_specs in services_set.iteritems():

        # Add service to main services list.
        # If the service name already exists we will override
        docker_services[service_name] = service_specs


for service_name, service_specs in docker_services:

    options = ""
    image = ""
    command = ""

    service_name_camelcase = underscore_to_camelcase(service_name)

    # We can't build a systemd service file without an image
    if "image" not in service_specs:
        continue

    # Save image and remove from service specs
    service_image = service_specs["image"]
    del service_specs["image"]

    # Get the run command if specified
    if "command" in service_specs:
        command = service_specs["command"]
        del service_specs["command"]

    for attr_name, attr_value in service_specs.iteritems():

        translator = None

        try:
            module = importlib.import_module('traductor.translators')
            translator = getattr(module, attr_name)
            translator = translator()
        except AttributeError:
            continue

        # Add returned string to docker run options
        options += " %s" % translator.translate(attr_value)


    # Build the systemd service file using Jinja2
    template_loader = jinja2.FileSystemLoader(searchpath=os.getcwd())
    template_env = jinja2.Environment(loader=template_loader)
    template_vars = {
        "service": {
            "name": image,
            "description": "% service" % service_name_camelcase,
            "image": image,
            "options": options,
            "command": command,
        }
    }

    # Render systemd service file
    template = template_env.get_template('templates/systemd.jinja2.service')
    output_text = template.render(template_vars)
    print(output_text, file=open("%s.service" % service_name, "w"))
    print(output_text)

