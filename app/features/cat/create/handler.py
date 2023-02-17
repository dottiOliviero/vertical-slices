from fastapi.routing import APIRoute
from fastapi.exceptions import HTTPException 
from .use_case import create_cat
from .models import CreateCatRequestBody, Cat



def create_cat_handler(cat: CreateCatRequestBody):
    result=create_cat(cat)
    if result:
        return Cat(result)
    raise HTTPException(status_code=420, detail="not able to create cat")



create_cat_route = APIRoute(
    path="/cat",
    endpoint=create_cat_handler,
    response_model=Cat,
    methods=["POST"],
)