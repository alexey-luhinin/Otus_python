'''Vehicle'''
from abc import ABC, abstractmethod
from vehicle_errors import (WeightTypeError,
                            PositiveError,
                            CarryingTypeError,
                            MileageTypeError,
                            NameTypeError,
                            EmptyStringError,
                            ProductionYearTypeError)


class Vehicle(ABC):
    '''Abstact class Vehicle'''

    def __init__(self,
                 name: str,
                 weight: float,
                 carrying: float,
                 production_year: int,
                 mileage: float
                 ):

        if not isinstance(name, str):
            raise NameTypeError

        if not name:
            raise EmptyStringError

        self._name = name

        if not isinstance(weight, (int, float)):
            raise WeightTypeError

        if weight < 0:
            raise PositiveError(weight)

        self._weight = weight

        if not isinstance(carrying, (int, float)):
            raise CarryingTypeError

        if carrying < 0:
            raise PositiveError(carrying)

        self._carrying = carrying

        if not isinstance(production_year, int):
            raise ProductionYearTypeError

        if production_year < 0:
            raise PositiveError(production_year)

        self._production_year = production_year

        if not isinstance(mileage, (int, float)):
            raise MileageTypeError

        if mileage < 0:
            raise PositiveError(mileage)

        self._mileage = mileage

    @property
    def name(self):
        '''name getter'''
        return self._name

    @property
    def weight(self):
        '''weight getter'''
        return self._weight

    @property
    def carrying(self):
        '''carrying getter'''
        return self._carrying

    @property
    def production_year(self):
        '''production_year getter'''
        return self._production_year

    @property
    def mileage(self):
        '''mileage getter'''
        return self._mileage

    @abstractmethod
    def move(self, distance: float):
        '''Move'''
        raise NotImplementedError

    @abstractmethod
    def make_a_sound(self):
        '''Make a sound'''
        raise NotImplementedError


if __name__ == '__main__':
    pass
