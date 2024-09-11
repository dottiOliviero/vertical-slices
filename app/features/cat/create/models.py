from typing import TypedDict


class CreateCatRequestBody(TypedDict):
    name: str
    age: int
    color: str

class Cat(CreateCatRequestBody):
    id: int

