# Traductor

A translator for docker-compose YAML files into process manager launch files (systemd supported so far).

##Features:
v1
- Responsability of operator to make sure services don't clash
- Input template defined in YAML
- Multiple systemd files generated with one command
- All known systemd DK Keys are supported
- Working systemd Unit File
- Using [Jinja2](http://jinja.pocoo.org/) for process manager template file generation

v2
- Multiple YAML files parsed at once
- Inject systemd files into the container
- Templated input
- Support for generating service files for other process managers

## Requirements
[Systemd-docker](https://github.com/ibuildthecloud/systemd-docker)

## Constraints
- Docker Compose does not support all the same arguments Docker run does

## Usage

### Build and Install

    $ python setup.py sdist
    # pip install dist/*.tar.gz

### Test

	python -m unittest discover tests -v
