from os import environ
from datetime import datetime
from fastapi import APIRouter, Request

router = APIRouter()

app_name = environ["APP_NAME"] = "simpleapi_py"
env_name = environ["ENV_NAME"] = "dev"


@router.get("/healthcheck")
async def healthcheck_route(request: Request):
    response = {
        "app": app_name,
        "env": env_name,
        "method": request.method,
        "path": request.url.path,
        "timestamp": datetime.now()
    }
    return response


@router.post("/healthcheck")
async def healthcheck_route(request: Request):
    response = {
        "app": app_name,
        "env": env_name,
        "method": request.method,
        "path": request.url.path,
        "timestamp": datetime.now()
    }
    return response
