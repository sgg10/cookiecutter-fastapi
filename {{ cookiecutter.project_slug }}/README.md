# {{cookiecutter.project_name}}

{{cookiecutter.description}}

[![Built with Cookiecutter](https://img.shields.io/badge/build%20with-Cookiecutter%20FastAPI-purple)](https://github.com/sgg10/cookiecutter-fastapi/)

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{%- if cookiecutter.open_source_license != "Not open source" %}

License: {{cookiecutter.open_source_license}}
{%- endif %}

## Table of contents
1. [Project structure](#structure)
2. [Environment variables](#environment)
3. [How to use](#howto)

## Project structure <a name="structure"></a>
<pre>
{{ cookiecutter.project_slug }}
├── app                          // FastAPI App directory
│   ├── api                      // Directory of parts
│   │   └── __init__.py
│   ├── core                     // Core of app
│   │   ├── settings             // Settings by ENV module
│   │   │   ├── base.py          // Base global setting for app
│   │   │   ├── __init__.py
│   │   │   ├── local.py         // Setting for local environment
│   │   │   └── production.py    // Setting for production environment
│   │   ├── config.py            // Global configuration for app
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py                  // Main app file
├── compose                      // Docker configuration by environment
│   ├── local
│   │   └── fastapi
│   │       ├── Dockerfile       // Docker file to local environment
│   │       └── start            // Script to start fastapi service
│   └── production
│       └── fastapi
│           ├── entrypoint       // Entrypoint to Docker in production
│           └── start            // Script to start fastapi service
├── .envs                        // ENV variables directory
│   ├── .local
│   │   ├── .app                 // FastAPI variables{% if cookiecutter.cloud_provider == "AWS" %}
│   │   ├── .aws                 // AWS variables{% endif %}{% if cookiecutter.database == "Postgres" %}
│   │   └── .postgres            // Postgress DB variables{% endif %}
│   └── .production
│       ├── .app                 // FastAPI variables{% if cookiecutter.cloud_provider == "AWS" %}
│       ├── .aws                 // AWS variables{% endif %}{% if cookiecutter.database == "Postgres" %}
│       └── .postgres            // Postgress DB variables{% endif %}
├── requirements                 // Recursive requirements
│   ├── base.txt                 // Base app requirements
│   ├── local.txt                // Local requirements
│   └── production.txt           // Production requirements
├── tests                        // Test Directory
│   └── __init__.py
├── docker-compose.yml           // Docker Compose to local development
├── Dockerfile                   // Docker file to production environment
├── .dockerignore
├── .editorconfig
├── .dockerignore
├── .editorconfig
├── LICENCE
├── .pre-commit-config.yaml
├── .pylintrc
├── README.md                    // This file
└── .setup.cfg
</pre>

## Environment variables <a name="environment"></a>
The environment variables are distributed in different files within path `./envs/.(local|production)/`

|Name|Type|File|Description|
|----|----|----|-----------|
|ENV|STR|.app|Switch between `local` and `production`|{% if cookiecutter.cloud_provider == "AWS" %}
|AWS_ACCESS_KEY|STR|.aws|Acces key account|
|AWS_SECRET_ACCESS_KEY|STR|.aws|Secret acces key account|
|AWS_DEFAULT_REGION|STR|.aws|Region by default|{% endif %}{% if cookiecutter.database == "Postgres" %}
|POSTGRES_HOST|STR|.postgres|Database host|
|POSTGRES_PORT|INT|.postgres|Database port|
|POSTGRES_DB|STR|.postgres|Database name. Default = `{{ cookiecutter.project_slug }}`|
|POSTGRES_USER|STR|.postgres|Database user|
|POSTGRES_PASSWORD|STR|.postgres|Database password|{% endif %}

## How to use <a name="howto"></a>

{% if cookiecutter.use_docker == "yes" %}
First, docker images must be created. `docker-compose.yml` can be use to build images
```bash
docker-compose build
```
After, you can use the following commands to start
```bash
docker-compose up
# Or docker-compose up -d to run in background
```
*Note*: You can stop project with
```bash
docker-compose down
```
{% else %}

*Note*: Before starting with application startup, it is recommended to use a virtual environment like `Venv` or `Pipenv`

First, install project dependencies.
```bash
pip install -r requirements/local.txt
# pipenv install -r requirements/local.txt if use Pipenv
```

After installing the dependencies, you can start the application

```bash
uvicorn app.main:app --port 8080 --reload
```

{% endif %}

Once executed, just access `localhost:8080`

### Tests
```bash
{% if cookiecutter.use_docker == "yes" %} docker-compose run --rm fastapi {% endif %}pytest
```

### Type Checks

Running type checks with mypy:

```bash
{% if cookiecutter.use_docker == "yes" %} docker-compose run --rm fastapi {% endif %}mypy {{ cookiecutter.project_slug }}
```

### Test Coverage
```bash
{% if cookiecutter.use_docker == "yes" %} docker-compose run --rm fastapi {% endif %}coverage run -m pytest
{% if cookiecutter.use_docker == "yes" %} docker-compose run --rm fastapi {% endif %}coverage html
```
After, open `htmlcov/index.html`.

### Flake8
```bash
{% if cookiecutter.use_docker == "yes" %} docker-compose run --rm fastapi {% endif %}flake8 path/to/code/
```
