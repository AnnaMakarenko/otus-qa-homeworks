import math

from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        super().__init__()
        self.name = "Triangle"

        if not (a + b > c or a + c > b or b + c > a):
            raise ValueError
        self.__a = a
        self.__b = b
        self.__c = c
        self.perimetr = self.get_perimetr()
        self.area = self.get_area()

    def get_perimetr(self) -> int or float:
        a = self.__a
        b = self.__b
        c = self.__c
        p = a + b + c
        return p

    def get_area(self) -> int or float:
        a = self.__a
        b = self.__b
        c = self.__c
        p = self.perimetr / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))  # sqrt -- импортированная функция для расчета квадратного корня
        return s


biba = Triangle(12, 13, 15)
boba = Triangle(11, 14, 15)

# print(biba.name)
# print(boba.name)
# print(biba.get_area())
# print(boba.get_area())
# print(biba.add_area(boba))
# print(boba.add_area(biba))
