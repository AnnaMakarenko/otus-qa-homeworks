class Figure:
    name = 'BaseClass'

    def add_area(self, v):
        if not isinstance(self.area, Figure):
            raise ValueError('Should be Figure!')
        else:
            return self.area + v.area

#Что еще нужно добавить, чтобы реализовать проверки на add area :(
