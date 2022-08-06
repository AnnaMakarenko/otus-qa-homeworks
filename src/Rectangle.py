from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = "Rectangle"
        self.__a = a
        self.__b = b
        self.perimetr = self.get_perimetr()
        self.area = self.get_area()

    def get_perimetr(self) -> int or float:
        a = self.__a
        b = self.__b
        p = (a + b) * 2
        return p

    def get_area(self) -> int or float:
        a = self.__a
        b = self.__b
        s = a * b
        return s
