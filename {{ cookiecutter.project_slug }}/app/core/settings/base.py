"""
Base settings
"""
from typing import Dict

import environ

from pydantic import BaseSettings


env = environ.Env()

# Base
class BaseAppSettings(BaseSettings):
    PREFIX: str = ""
    app_name: str = '{{ cookiecutter.project_name }}'
    version: str = '{{ cookiecutter.version }}'
    author: Dict[str, str] = {
        "name": '{{ cookiecutter.author_name }}',
        "nickname": '{{ cookiecutter.author_nickname }}',
        "domain": '{{ cookiecutter.domain_name }}',
        "email": '{{ cookiecutter.email }}'
    }
