import math

from src.Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        self.name = "Circle"

        self.__r = r
        self.perimetr = self.get_perimetr()
        self.area = self.get_area()

    def get_perimetr(self) -> int or float:
        r = self.__r
        p = 2 * r * math.pi
        return p

    def get_area(self) -> int or float:
        r = self.__r
        s = math.pi * r ** 2
        return s
