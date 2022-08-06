from src.Circle import *


def test_area_circle_ok():
    res = Circle(13)
    assert round(res.area, 2) == 530.93


def test_area_circle_perimetr_ok():
    res = Circle(3.1)
    assert round(res.area, 2) == 30.19
