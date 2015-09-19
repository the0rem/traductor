import yaml
import argparse

from jinja2 import Template

from . import translators


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

