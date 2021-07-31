'''Task 1'''
import time
from typing import List
from functools import wraps


def powers(*args: int, power: int = 2) -> list:
    '''Takes N numbers and raises them to a power.'''
    return [n**power for n in args]


def even_odd_prime(numbers: List[int], type_of_out='prime') -> List[int]:
    '''Takes list of intergers and returns filtered numbers
       by type[prime, odd, even]'''

    if type_of_out == 'even':
        return list(filter(lambda x: x % 2 == 0, numbers))

    if type_of_out == 'odd':
        return list(filter(lambda x: x % 2 != 0, numbers))

    if type_of_out == 'prime':
        primes = []
        for number in numbers:
            if number <= 1:
                continue
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
        return primes

    return None


def time_meter(func):
    '''Decorator for time measurement.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        end = time.monotonic()
        print(f'Function "{func.__name__}" takes {end-start} seconds.')
        return result
    return wrapper
