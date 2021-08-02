'''Vehicle'''
from abc import ABC, abstractmethod


class Vehicle(ABC):
    '''Abstact class Vehicle'''

    def __init__(self,
                 name: str,
                 weight: float,
                 carrying: float,
                 production_year: int
                 ):
        self._name = name
        self._weight = weight
        self._carrying = carrying
        self._production_year = production_year

    @property
    def name(self):
        '''name getter'''
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def weight(self):
        '''weight getter'''
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def carrying(self):
        '''carrying getter'''
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying

    @property
    def production_year(self):
        '''production_year getter'''
        return self._production_year

    @production_year.setter
    def production_year(self, production_year):
        self._production_year = production_year

    @abstractmethod
    def start_engine(self):
        '''Start engine'''
        raise NotImplementedError

    @abstractmethod
    def turn_off_engine(self):
        '''Turn off engine'''
        raise NotImplementedError

    @abstractmethod
    def make_a_sound(self):
        '''Make a sound'''
        raise NotImplementedError


if __name__ == '__main__':
    pass