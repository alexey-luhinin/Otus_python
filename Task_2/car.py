'''Car'''
from vehicle import Vehicle
from vehicle_errors import (ModelTypeError,
                            PositiveError,
                            VinTypeError,
                            EmptyStringError,
                            DistanceTypeError)


class Car(Vehicle):
    '''Car'''

    WHEELS = 4

    def __init__(self, model: str, vin: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(model, str):
            raise ModelTypeError

        if not model:
            raise EmptyStringError

        self._model = model

        if not isinstance(vin, str):
            raise VinTypeError

        if not vin:
            raise EmptyStringError

        self._vin = vin

    @property
    def model(self):
        '''model getter'''
        return self._model

    @property
    def vin(self):
        '''vin getter'''
        return self._vin

    def move(self, distance: float):
        if not isinstance(distance, (int, float)):
            raise DistanceTypeError

        if distance < 0:
            raise PositiveError(distance)

        print(f'{self.name} is move')
        self._mileage += distance

    def make_a_sound(self):
        print('Car sound')

    def __str__(self):
        return f'Car(Name = {self.name}, '\
               f'Model = {self.model}, '\
               f'Production year = {self.production_year}, '\
               f'Mileage = {self.mileage}, '\
               f'vin = {self.vin})'


if __name__ == '__main__':
    tesla = Car('Model S', 'VK12323541', 'Tesla', 2000, 300, 2010, 100)
    volga = Car('Black', 'Volga123', 'Volga', 3000, 200, 1990, 500)
    print(tesla)
    tesla.move(25)
    print(tesla.mileage)
    print(volga)
