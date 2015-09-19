# traductor


##Notes:
v1
- Responsability of operator to make sure services don't clash
- Input template defined in YAML
- Multiple systemd files generated with one command
- Multiple YAML files parsed at once
- All known systemd DK Keys are supported
- Working systemd Unit File
- Using [Jinja2(http://jinja.pocoo.org/)] for systemd template file generation

v2
- Inject systemd files into the container
- Docker Composer does not support all the same arguments Docker Run does
- Templated Input

## Usage

### Build and Install

    $ python setup.py sdist
    # pip install dist/*.tar.gz
