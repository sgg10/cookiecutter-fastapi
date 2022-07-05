<!-- omit in toc -->
# Cookiecutter FastAPI <a name="cookiecutter-fastapi"></a>
![](https://img.shields.io/badge/license-MIT-green)
![](https://img.shields.io/badge/python-v3.9-blue)

FastAPI project creator for bigger apps

## Table of contents
- [References](#references)

## Features
- [x] For FastAPI 0.78.0
- [x] Works with Python 3.9
- [x] Docker support using [docker-compose](https://github.com/docker/compose) for development
- [x] Run tests with pytest
- [x] Integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
- [x] AWS connection
- [x] Postgres variables to connection
- [ ] GCP connection (coming soon!)
- [ ] CI tools (coming soon!)

## How to use

First, get Cookiecutter.
```bash
pip install cookiecutter
```

Now run it against this repository
```bash
cookiecutter https://github.com/sgg10/cookiecutter-fastapi
```

You'll be prompted for some values. Provide them, then a FastAPI project will be created for you.

# References
- For issues: [pre-commit](https://github.com/pre-commit/pre-commit)
- For Docker Support: [docker-compose](https://github.com/docker/compose)
- For Testing: [pytest](https://github.com/pytest-dev/pytest)
- For projects creation: [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Inpired by [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)