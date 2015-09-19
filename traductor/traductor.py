#! /usr/bin/env python

from __future__ import print_function

import os
import sys
import yaml
import jinja2
import argparse
import importlib

from exceptions import AttributeError


class Traductor(object):
    """
    Handles logic for translating docker-compose yaml files to systemd services
    """
    def underscore_to_camelcase(self, value):
        """
        Translate a snake_case to CamelCase
        """
        def upperfirst(x):
            return x[0].upper() + x[1:]
        def camelcase():
            yield str.lower
            while True:
                yield str.capitalize
        c = camelcase()
        return upperfirst("".join(c.next()(x) if x else '_' for x in value.split("_")))


    def translate(self, files):
        """

        """
        docker_services = {}

        # Loop through given files
        for file in files:

            # Load YAML into python
            with open(file, 'r') as stream:
                services_set = yaml.load(stream)

            # Loop through services from YAML file
            for service_name, service_specs in services_set.iteritems():

                # Add service to main services list.
                # If the service name already exists we will override
                docker_services[service_name] = service_specs


        for service_name, service_specs in docker_services.iteritems():

            image = ""
            options = ""
            command = ""

            # Save image and remove from service specs
            if "image" in service_specs:
                image = service_specs["image"]
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
                    "description": "% service" % self.underscore_to_camelcase(service_name),
                    "image": image,
                    "options": options,
                    "command": command,
                }
            }

            # Render systemd service file
            template_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates/systemd.jinja2.service")
            print('%s' % template_file)
            template = template_env.get_template(template_file)
            output_text = template.render(template_vars)
            print(output_text, file=open("%s.service" % service_name, "w"))
            print(output_text)


class Cli(object):
    """
    Cli handler
    """
    def __init__(self):
        # Setup cli handler
        parser = argparse.ArgumentParser(description="Translate docker-compose templates to process manage service files " \
            "(systemd currently supported).")

        parser.add_argument(
            '-f',
            '--file',
            dest='file',
            help='Specify docker-compose files (default: docker-compose.yml)',
            default='docker-compose.yml',
        )

        # Get cli arguments
        args = parser.parse_args()

        Traductor().translate(files=[args.file])


if __name__ == "__main__":
    Cli()