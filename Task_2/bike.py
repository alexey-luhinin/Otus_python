'''Bike'''
from vehicle import Vehicle
from vehicle_errors import (ModelTypeError,
                            EmptyStringError,
                            PositiveError,
                            DistanceTypeError)


class Bike(Vehicle):
    '''Bike'''
    WHEELS = 2

    def __init__(self, model: str, *args, **kwargs):
        super().__init__(*args, *kwargs)

        if not isinstance(model, str):
            raise ModelTypeError

        if not model:
            raise EmptyStringError

        self._model = model

    @property
    def model(self):
        '''model getter'''
        return self._model

    def move(self, distance):

        if not isinstance(distance, (int, float)):
            raise DistanceTypeError

        if distance < 0:
            raise PositiveError(distance)

        self._mileage += distance

    def make_a_sound(self):
        print('Ridding bike sound')

    def __str__(self):
        return f'Bike(name = {self.name},'\
               f'model = {self.model}, '\
               f'production year = {self.production_year})'


if __name__ == '__main__':
    bike = Bike('Corsair', 'Ardis', 20, 5, 2019, 10)
    bike.move(4)
    print(bike.mileage)
    print(bike.make_a_sound())
