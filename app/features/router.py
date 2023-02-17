from fastapi import APIRouter
from app.features.cat.router import cat_router

router = APIRouter()
router.include_router(router=cat_router, tags=["cat"])