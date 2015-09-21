# Traductor

A translator for docker-compose YAML files into process manager launch files (systemd supported so far).

This helps support running docker containers as services under the OS' process manager (such as systemd).
This can extend into being able to package docker containers as rpms for install.

##Features:
v1
- Responsability of operator to make sure services don't clash
- Input template defined in YAML
- Multiple systemd files generated with one command
- All known systemd DK Keys are supported
- Working systemd Unit File
- Using [Jinja2](http://jinja.pocoo.org/) for process manager template file generation
- Multiple docker-compose YAML files parsed at once

v2
- Inject systemd files into the container
- Templated input
- Support for generating service files for other process managers
- RPM generation

## Requirements
To run the systemd service files you will need to install [systemd-docker](https://github.com/ibuildthecloud/systemd-docker). This is a wrapper around docker which solves the following problem of running docker containers under systemd:
> Systemd does not actually supervise the Docker container but instead the Docker client. This makes systemd incapable of reliably managing Docker containers without hitting a bunch of really odd situations.

## Constraints
- Docker Compose does not support all the same arguments Docker run does

## Usage

### Build and Install

    $ python setup.py sdist
    # pip install dist/*.tar.gz

### Test

	python -m unittest discover tests -v
