# django-starter-oidc-authserver

OpenID Connect authorization server written in Python (Django). This project is part of a 
bundle of services that I'm developing for learning purposes only. Once 
finished, this repository could be a starting point for a custom 
authorization server.

### Technology stack
- docker
- django
- postgresql
- nginx
- supervisor

## Disclaimer

Files included in this repository are meant to be used in local
environment only. Please ensure all passwords or keys included here are not
used in production.

### List of files that include keys/passwords/secrets
- ./local/docker/fixtures/fixtures.json
- ./local/compose.yml
- ./secrets/*

## Installation

```shell
# create virtual environment
python3 -m venv .venv

# activate virtual environment
. .venv/bin/activate

# install requirements
pip install -r requirements.txt

# install and run services
. ./local/scripts/install
```

## Build image to use in other local projects

```shell
# execute script
. ./local/scripts/build-local-portable-image
```

## Related projects

- Resource server [spring-starter-oidc-resourceserver](https://github.com/emidiocruciani/spring-starter-oidc-resourceserver/)
- Frontend app [angular-starter-oidc-app](https://github.com/emidiocruciani/angular-starter-oidc-app/)
