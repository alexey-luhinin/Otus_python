'''Task 1'''


def powers(*args: int, power: int = 2) -> list:
    '''Takes N numbers and raises them to a power.'''
    return [n**power for n in args]
