from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def main_route(request: Request):
    response = {
        "method": request.method,
        "path": request.url.path
    }
    return response


@router.post("/")
async def main_route(request: Request):
    response = {
        "method": request.method,
        "path": request.url.path
    }
    return response
