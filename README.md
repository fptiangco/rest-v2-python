[![codecov](https://codecov.io/gh/fptiangco/rest-v2-python/branch/main/graph/badge.svg?token=XBB48QQDSM)](https://codecov.io/gh/fptiangco/rest-v2-python) [![Push](https://github.com/fptiangco/rest-v2-python/actions/workflows/trigger_push.yaml/badge.svg)](https://github.com/fptiangco/rest-v2-python/actions/workflows/trigger_push.yaml) [![Docker](https://img.shields.io/docker/cloud/build/fptiangco/rest-v2-python?label=Docker&style=flat)](https://hub.docker.com/r/fptiangco/rest-v2-python/builds)

Quickstart

Local/Virtualenv:
```
# Install
pip install -r src/requirements.txt
# Test and Coverage
pytest --cov
# Run
export FLASK_APP=src/server.py; flask run -h 0.0.0.0 -p 5000
```
Docker
```
# Build
docker build . -t rest-v2-python
# Test
docker run rest-v2-python pytest --cov
# Run
docker run -p 5000:5000 rest-v2-python
```