from fastapi import APIRouter
from .create.handler import create_cat_route

cat_router = APIRouter(
    routes=[
    create_cat_route
    ])
