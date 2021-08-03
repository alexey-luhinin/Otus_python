'''Tank'''
from dataclasses import dataclass
from vehicle_errors import PositiveError, TankOverflowError


@dataclass
class Tank:
    '''Tank'''
    max_volume: float
    volume: float

    def add_fuel(self, fuel):
        '''Add fuel to tank'''
        if fuel < 0:
            raise PositiveError(fuel)
        if self.volume + fuel > self.max_volume:
            raise TankOverflowError
        self.volume += fuel
        print('Fuel volume:', self.volume)
