import pytest

from src.Rectangle import *
from src.Triangle import *

RES_TR = Triangle(13, 14, 15)
RES_RC = Rectangle(13, 14)


def test_add_area_ok():
    assert RES_TR.add_area(RES_RC) == 266


def test_add_area_object_error():
    with pytest.raises(ValueError) as exc_info:
        RES_TR.add_area(1)
    assert ValueError
