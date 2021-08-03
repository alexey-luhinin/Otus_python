'''Airplane'''
from vehicle import Vehicle
from vehicle_errors import (ModelTypeError,
                            EmptyStringError,
                            PositiveError,
                            DistanceTypeError,
                            MaxHeighTypeError)


class Airplane(Vehicle):
    '''Airplane'''
    def __init__(self, model: str, max_height: float, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(model, str):
            raise ModelTypeError

        if not model:
            raise EmptyStringError

        self._model = model

        if not isinstance(max_height, (int, float)):
            raise MaxHeighTypeError

        if max_height < 0:
            raise PositiveError(max_height)

    @property
    def model(self):
        '''model getter'''
        return self._model

    def move(self, distance: float):
        if not isinstance(distance, (int, float)):
            raise DistanceTypeError

        if distance < 0:
            raise PositiveError(distance)

        self._mileage += distance

    def make_a_sound(self):
        print('''Airplane sounding''')

    def __str__(self):
        return f'Airplane(Name = {self.name}, '\
               f'Model = {self.model}, '\
               f'Production year = {self.production_year}, '\
               f'Mileage = {self.mileage}) '


if __name__ == '__main__':
    ty124 = Airplane('Ty-124', 15000, 'Ty', 5000, 1000, 1999, 20000)
    print(ty124)
    ty124.move(200)
    print(ty124.mileage)
