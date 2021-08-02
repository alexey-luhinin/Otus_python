from vehicle import Vehicle


class Car(Vehicle):
    '''Car'''

    WHEELS = 4

    def __init__(self, model: str, VIN: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = model
        self._VIN = VIN

    @property
    def model(self):
        return self._model

    @property
    def VIN(self):
        return self._VIN

    def start_engine(self):
        print('Tesla is ready to move')

    def turn_off_engine(self):
        print('Tesla off now')

    def make_a_sound(self):
        print('Silent')

    def __str__(self):
        return f'Car(Name = {self.name}, '\
               f'Model = {self.model}, '\
               f'Production year = {self.production_year}, '\
               f'VIN = {self.VIN})'


if __name__ == '__main__':
    tesla = Car('Model S', 'KN11911155', 'Tesla', 2000, 300, 2010)
    print(tesla)
