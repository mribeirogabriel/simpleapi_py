import uvicorn

from fastapi import FastAPI
from src.routers import root, health

app = FastAPI()
app.include_router(root.router)
app.include_router(health.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
