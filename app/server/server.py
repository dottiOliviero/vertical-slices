from fastapi import FastAPI
from app.features.router import router

def create_server():
    fastapi_app = FastAPI()
    fastapi_app.include_router(router, prefix="/v1")

    return fastapi_app