| | |
|---|---|
| Tests | [![codecov](https://codecov.io/gh/fptiangco/rest-v2-python/branch/main/graph/badge.svg?token=XBB48QQDSM)](https://codecov.io/gh/fptiangco/rest-v2-python) [![Push](https://github.com/fptiangco/rest-v2-python/actions/workflows/trigger_push.yaml/badge.svg)](https://github.com/fptiangco/rest-v2-python/actions/workflows/trigger_push.yaml) |
| Docker | [![Docker](https://img.shields.io/docker/cloud/build/fptiangco/rest-v2-python?label=Docker&style=flat)](https://hub.docker.com/r/fptiangco/rest-v2-python/builds) ![Docker Pulls](https://img.shields.io/docker/pulls/fptiangco/rest-v2-python) ![Docker Image Version (latest semver)](https://img.shields.io/docker/v/fptiangco/rest-v2-python?sort=semver) |
| QA | [![Updates](https://pyup.io/repos/github/fptiangco/rest-v2-python/shield.svg)](https://pyup.io/repos/github/fptiangco/rest-v2-python/) |
| Code | <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> |
| Scans | [![Updates](https://pyup.io/repos/github/fptiangco/rest-v2-python/shield.svg)](https://pyup.io/repos/github/fptiangco/rest-v2-python/)|



### Quickstart
* A utility service that returns 'v2'

##### Local flask run
```
# Install
pip install -r requirements.txt

# Python package scan
safety check
# Test and coverage
pytest --cov

# Run on localhost:5000
export FLASK_APP=src/server.py; flask run -h 0.0.0.0 -p 5000
```
##### Docker build + run
```
# Build
docker build . -t rest-v2-python

# Image scan
docker scan rest-v2-python
# Python package scan
docker run rest-v2-python safety check
# Test and coverage
docker run rest-v2-python pytest --cov

# Run on localhost:5000
docker run -p 5000:5000 rest-v2-python
```
##### Dockerhub run
```
docker run -p 5000:5000 fptiangco/rest-v2-python
```
##### View
http://localhost:5000
