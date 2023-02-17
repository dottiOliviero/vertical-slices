from app.features.cat.create.use_case import create_cat
from app.features.cat.create.models import CreateCatRequestBody


def test_create_cat_uc_success():
    create_cat_request = CreateCatRequestBody(name="pino", age=9, colo="black")

    result = create_cat(cat=create_cat_request)
    assert result == {"id": 1, "name": "pino", "age": 9, "colo": "black"}
