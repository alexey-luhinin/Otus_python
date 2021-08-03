'''Vehicle errors'''


class WeightTypeError(TypeError):
    '''WeightTypeError'''


class CarryingTypeError(TypeError):
    '''CarryingTypeError'''


class MileageTypeError(TypeError):
    '''MileageTypeError'''


class ProductionYearTypeError(TypeError):
    '''ProductionYearTypeError'''


class NameTypeError(TypeError):
    '''NameTypeError'''


class VinTypeError(TypeError):
    '''VinTypeError'''


class ModelTypeError(TypeError):
    '''ModelTypeError'''


class PositiveError(ValueError):
    '''PositiveError'''
    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__value = value

    def __str__(self):
        return f'Value can\'t be negative. Input {self.__value}'


class EmptyStringError(ValueError):
    '''EmptyStringError'''
