import pytest

from src.Triangle import *


# проверка имени класса
def test_triangle_name():
    t = Triangle(11, 12, 13)
    assert t.name == "Triangle"


# проверка на ошибку при невалидных данных
def test_rectangle_value_error():
    with pytest.raises(ValueError) as exc_info:
        Triangle(10, 5, 3)
    assert ValueError


# простая проверка значений площади
def test_area_triangle_ok():
    res = Triangle(13, 14, 15)
    assert res.area == 84


# проверка другим способом, с параметрайзом на площадь
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (12, 13, 15), 74.83,
        id="general",
    ),
    pytest.param(
        (5, 3.1, 2), 1.23,
        id="float",
    ),
])
def test_triangle_area_value(params, expected_result):
    res = Triangle(*params)
    f = res.get_area()
    assert round(f, 2) == expected_result


# проверка с параметрайзом на периметр
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (12, 13, 15), 40,
        id="general",
    ),
    pytest.param(
        (5, 3.1, 2), 10.1,
        id="float",
    ),
])
def test_triangle_perimetr_value(params, expected_result):
    res = Triangle(*params)
    f = res.get_perimetr()
    assert round(f, 2) == expected_result
