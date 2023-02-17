from typing import TypedDict
from fastapi.routing import APIRoute
from random import randint

class CreateCatRequestBody(TypedDict):
    name: str
    age: int
    color: str

class Cat(CreateCatRequestBody):
    id: int

def create_cat_handler(cat: CreateCatRequestBody):
    return Cat(id=randint(1,100), **cat)



create_cat_route = APIRoute(
    path="/",
    endpoint=create_cat_handler,
    response_model=Cat,
    methods=["POST"],
)