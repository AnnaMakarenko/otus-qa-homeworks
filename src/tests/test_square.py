import pytest

from src.Square import *


@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (13), 169,
        id="general",
    ),
    pytest.param(
        (3.1), 9.61,
        id="float",
    ),
])
def test_triangle_area_value(params, expected_result):
    res = Square(params)
    f = res.get_area()
    assert round(f, 2) == expected_result


@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (12), 48,
        id="general",
    ),
    pytest.param(
        (3.1), 12.4,
        id="float",
    ),
])
def test_triangle_perimetr_value(params, expected_result):
    res = Square(params)
    f = res.get_perimetr()
    assert round(f, 2) == expected_result
