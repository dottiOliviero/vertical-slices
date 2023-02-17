from fastapi import APIRouter
from .create.create import create_cat_route

cat_router = APIRouter(prefix="/cat")

cat_router.routes = [create_cat_route]