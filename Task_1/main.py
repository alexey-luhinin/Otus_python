'''Task 1'''


def powers(*args: int, power=2) -> list:
    '''Takes N int and powers them by power.'''
    return [n**power for n in args]
