from unittest import TestCase
from Triangle import Triangle
from Rectangle import Rectangle, TYPE_ERROR_TEXT1, TYPE_ERROR_TEXT2
from Square import Square
from Circle import Circle

import pytest


# class TestAddCase(TestCase):
#     def test_ok(self):
#         res = Triangle(13, 14, 15)
#         self.assertEqual(res.area, 84)


def test_area_triangle_ok(*args):
    res = Triangle(13, 14, 15)
    assert res.area == 84

#ПРЯМОУГОЛЬНИК
# Прямоугольник - тест на отрицательные значения
def test_rectangle_raise_error_zero(*args):
    with pytest.raises(ValueError) as exc_info:
        Rectangle(-1, 1)
    assert str(exc_info.value) == TYPE_ERROR_TEXT2

# Прямоугольник - тест на тип вводимых данных
def test_rectangle_raise_error_type(*args):
    with pytest.raises(ValueError) as exc_info:
        Rectangle('3', 1)
    assert str(exc_info.value) == TYPE_ERROR_TEXT1


# ПОЧЕМУ НЕ РАБОТАЕТ ТАКОЙ ВЫВОД? через периметр
# def test_rectangle_raise_error_type(*args):
#     with pytest.raises(TypeError) as exc_info:
#         (Rectangle.perimeter)(-1,-1)
#     assert str(exc_info.value) == TYPE_ERROR_TEXT1


# Прямоугольник - периметр: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (4, 4), 16,
        id="general",
    ),
    pytest.param(
        (3.1, 1), 8.2,
        id="float",
    ),
])
def test_rectangle_value(params, expected_result):
    res = Rectangle(*params)
    assert res.perimeter == expected_result

# Прямоугольник - площадь: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (4, 4), 16,
        id="general",
    ),
    pytest.param(
        (3.1, 1), 3.1,
        id="float",
    ),
])
def test_rectangle_value(params, expected_result):
    res = Rectangle(*params)
    assert res.area == expected_result


# КВАДРАТ
# Квадрат - тест на отрицательные значения
def test_square_raise_error_zero(*args):
    with pytest.raises(ValueError) as exc_info:
        Square(-1)
    assert str(exc_info.value) == TYPE_ERROR_TEXT2

# Квадрат - тест на тип вводимых данных
def test_square_raise_error_type(*args):
    with pytest.raises(ValueError) as exc_info:
        Square('3')
    assert str(exc_info.value) == TYPE_ERROR_TEXT1


# Квадрат - периметр: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (4), 16,
        id="general",
    ),
    pytest.param(
        (3.1), 12.4,
        id="float",
    ),
])
def test_square_value(params, expected_result):
    res = Square(params)
    assert res.perimeter == expected_result



# Квадрат - площадь: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (5), 25,
        id="general",
    ),
    pytest.param(
        (3.1), 9.61,
        id="float",
    ),
])
def test_square_value(params, expected_result):
    res = Square(params)
    assert round(res.area, 2) == expected_result



# КРУГ
# КРУГ - тест на отрицательные значения
def test_сircle_raise_error_zero(*args):
    with pytest.raises(ValueError) as exc_info:
        Circle(-1)
    assert str(exc_info.value) == TYPE_ERROR_TEXT2

# Квадрат - тест на тип вводимых данных
def test_сircle_raise_error_type(*args):
    with pytest.raises(ValueError) as exc_info:
        Circle('3')
    assert str(exc_info.value) == TYPE_ERROR_TEXT1


# Круг - периметр: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (4), 16,
        id="int",
    ),
    pytest.param(
        (3.1), 19.48,
        id="float",
    ),
])
def test_circle_value(params, expected_result):
    res = Circle(params)
    assert round(res.perimeter, 2) == expected_result



# Круг - площадь: позитивный тест на int и float и на верность расчета
@pytest.mark.parametrize("params, expected_result", [
    pytest.param(
        (5), 78.54,
        id="int",
    ),
    pytest.param(
        (3.1), 30.19,
        id="float",
    ),
])
def test_circle_value(params, expected_result):
    res = Circle(params)
    assert round(res.area, 2) == expected_result


def figure_area_ok()
    res = Figure.add_area()
    assert res