from Figure import Figure
from math import pi


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        self.radius = radius
        if not isinstance(self.radius, (int, float)):
            raise ValueError('Введите чиcло')
        if self.radius <= 0:
            raise ValueError('Введите чиcло больше нуля')

    @property
    def perimeter(self):
        return 2 * self.radius * pi

    @property
    def area(self):
        return self.radius**2 * pi

    # def perimeter(self):
    #     return 2 * self.radius * pi
    #
    # def area(self):
    #     return self.radius ** 2 * pi


c = Circle(3)

print(c.area)
