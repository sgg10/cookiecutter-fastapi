from pathlib import Path

from settings.base import env
from settings.local import Settings as LocalSettings
from settings.production import Settings as ProductionSettings

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent

DATABASES = {
    {% if cookiecutter.database == "Postgres" %}
    env("POSTGRES_DB"): {
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
        "DB": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "ENGINE": "postgres"
    }
    {% endif %}
}

settings_class = LocalSettings
if env("ENV") == "production":
    settings_class = ProductionSettings

settings = settings_class()
