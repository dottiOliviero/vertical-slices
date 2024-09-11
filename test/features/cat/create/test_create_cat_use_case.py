from app.features.cat.create.models import CreateCatRequestBody
from app.features.cat.create.use_case import create_cat


def test_create_cat_uc_success(get_cursor_generator_test):
    create_cat_request = CreateCatRequestBody(name="pino", age=9, colo="black")
    # any_num_condition = AnyNumberWithCondition(condition=lambda x: x < 0)
    result = create_cat(cat=create_cat_request)
    assert result["id"] == AnyNumber()
    assert result["name"] == "pino"
    assert result["age"] == 9
    assert result["color"] == "black"


class AnyNumber:
    def __eq__(self, other):
        assert isinstance(other, int)
        return True

class AnyNumberWithCondition:
    # def __init__(self, condition=lambda x: x):
    #     self.condition = condition

    def __eq__(self, other):
        assert isinstance(other, int)
        # return self.condition(other)
