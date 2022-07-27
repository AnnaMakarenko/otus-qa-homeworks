from Figure import Figure

TYPE_ERROR_TEXT2 = 'Введите чиcло больше нуля'
TYPE_ERROR_TEXT1 = 'Введите чиcло'


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, side_x, side_y):
        self.side_x = side_x
        self.side_y = side_y
        if not isinstance(self.side_x, (int, float)) or not isinstance(self.side_y, (int, float)):
            raise ValueError(TYPE_ERROR_TEXT1)
        if self.side_x <= 0 or self.side_y <= 0:
            raise ValueError(TYPE_ERROR_TEXT2)

    @property
    def perimeter(self):
        return (self.side_x + self.side_y) * 2

    @property
    def area(self):
        return self.side_x * self.side_y

# r = Rectangle(2,4)
# print(r.perimeter_rectangle)
# print((Rectangle.perimeter_rectangle)(2, 4))

# print(Rectangle.area)

# x = Rectangle('4', 4)
# #
# print(x.area)
