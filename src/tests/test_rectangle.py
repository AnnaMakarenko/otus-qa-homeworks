import pytest

from src.Rectangle import *


# простая проверка
def test_area_triangle_ok():
    res = Rectangle(13, 14)
    assert res.area == 182


# проверка с параметрайзом
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (13, 14), 182,
        id="general",
    ),
    pytest.param(
        (5, 3.1), 197.5,
        id="float",
    ),
])
def test_triangle_area_value(params, expected_result):
    res = Rectangle(*params)
    f = res.get_area()
    assert round(f, 2) == expected_result


@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (12, 13), 50,
        id="general",
    ),
    pytest.param(
        (5, 3.1), 16.2,
        id="float",
    ),
])
def test_triangle_perimetr_value(params, expected_result):
    res = Rectangle(*params)
    f = res.get_perimetr()
    assert round(f, 2) == expected_result
