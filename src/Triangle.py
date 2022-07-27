from Figure import Figure

from Square import Square

#ВОПРОС: Каким образом лучше инициализировать функции? (как в файле треугольника или как в других)
# и через функции или методы обозначать периметр и площадь?

class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.perimeter = a + b + c
            p = self.perimeter / 2
            self.area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            raise ValueError


# triangle = Triangle(13, 14, 15)
#
# print(triangle.area)
# square = Square(50)
# print(triangle.add_area(square))
