from src.Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.name = "Square"
        self.__a = a
        self.perimetr = self.get_perimetr()
        self.area = self.get_area()

    def get_perimetr(self) -> int or float:
        a = self.__a
        p = a * 4
        return p

    def get_area(self) -> int or float:
        a = self.__a
        s = a ** 2
        return s
