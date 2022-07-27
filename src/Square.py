from Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, side_x):
        self.side_x = side_x
        if not isinstance(self.side_x, (int, float)):
            raise ValueError('Введите чиcло')
        if self.side_x <= 0:
            raise ValueError('Введите чиcло больше нуля')

    @property
    def perimeter(self):
        return (self.side_x * 4)

    @property
    def area(self):
        return self.side_x ** 2