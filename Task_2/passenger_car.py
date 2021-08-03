'''Passenger car'''
from car import Car
from engine import Engine
from tank import Tank
from vehicle_errors import PositiveError


class PassengerCar(Car):
    '''PassengerCar'''

    def __init__(self, fuel: float, engine: Engine,
                 tank: Tank, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if fuel < 0:
            raise PositiveError(fuel)

        self._fuel = fuel
        self._engine = engine
        self._tank = tank

    def start_car(self):
        '''start car'''
        if self._fuel > 0:
            self._engine.start()
        else:
            print('No fuel in the car')

    def stop_car(self):
        '''stop car'''
        if self._engine.is_worked:
            self._engine.stop()
        else:
            print('Engine already is off')

    def move(self, fuel_per_km: float, distance: float):
        if self._tank.volume - fuel_per_km * distance <= 0:
            raise PositiveError('Not enough fuel in the car')
        print('Car starting moving')
        self._tank.volume -= fuel_per_km * distance
        print(f'Car moved {distance} km, spend fuel {fuel_per_km * distance}')


    def refueling(self, fuel):
        print('Refueling...')
        self._tank.add_fuel(fuel)


if __name__ == '__main__':
    diesel_engine = Engine()
    tank = Tank(100, 20)
    mersedes = PassengerCar(50, diesel_engine, tank, 'W201', 'M8823223', 
                            'Mersedes', 2000, 500, 1990, 400000)
    print(mersedes)
    mersedes.start_car()
    mersedes.move(0.3, 10)
    mersedes.stop_car()
    mersedes.refueling(30)
