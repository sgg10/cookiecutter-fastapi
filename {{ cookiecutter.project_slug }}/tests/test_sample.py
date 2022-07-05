from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to {{ cookiecutter.project_name }} | Version: {{ cookiecutter.version }}"
    }

def test_author():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {
        "name": '{{ cookiecutter.author_name }}',
        "nickname": '{{ cookiecutter.author_nickname }}',
        "domain": '{{ cookiecutter.domain_name }}',
        "email": '{{ cookiecutter.email }}'
    }
