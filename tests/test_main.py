from src.main import app
from os import environ
from datetime import datetime
from fastapi.testclient import TestClient
from freezegun import freeze_time

client = TestClient(app)

app_name = environ["APP_NAME"] = "simpleapi_py"
env_name = environ["ENV_NAME"] = "dev"


def test_main_route():
    response = client.get("/")
    response_assert = {
        "method": "GET",
        "path": "/"
    }
    assert response.status_code == 200
    assert response.json() == response_assert


def test_main_route():
    response = client.post("/")
    response_assert = {
        "method": "POST",
        "path": "/"
    }
    assert response.status_code == 200
    assert response.json() == response_assert


@freeze_time("2022-09-09T18:51:16.661415")
def test_health_route():
    response = client.get("/healthcheck")
    response_assert = {
        "app": app_name,
        "env": env_name,
        "method": "GET",
        "path": "/healthcheck",
        "timestamp": datetime.now().isoformat()
    }
    assert response.status_code == 200
    assert response.json() == response_assert


@freeze_time("2022-09-09T18:51:16.661415")
def test_health_route():
    response = client.post("/healthcheck")
    response_assert = {
        "app": app_name,
        "env": env_name,
        "method": "POST",
        "path": "/healthcheck",
        "timestamp": datetime.now().isoformat()
    }
    assert response.status_code == 200
    assert response.json() == response_assert
