class Figure:
    def __init__(self):
        self.name = 'BaseClass'

    def area(self):
        return

    def add_area(self, figure: object):
        if not isinstance(figure, Figure):
            raise ValueError('Should be Figure!')
        else:
            my_area = self.get_area()
            figure_area: object = figure.get_area()
            return my_area + figure_area
