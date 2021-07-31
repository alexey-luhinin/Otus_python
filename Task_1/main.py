'''Task 1'''
import time
from typing import List
from functools import wraps


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


@time_meter
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


def trace(func):
    '''Trace decorator'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('-> {}({})'.format(func.__name__, *args))
        return func(*args, **kwargs)
    return wrapper


@trace
def fibonacci(number: int) -> int:
    '''Returns N number of fibonacci sequence.'''
    if number <= 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    print('Squred:', powers(1, 2, 3, 4, 5))
    print('Cubed:', powers(1, 2, 3, 4, 5, power=3))
    print('Even:', even_odd_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                  type_of_out='even'))
    print('Odd:', even_odd_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 type_of_out='odd'))
    print('Prime:', even_odd_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                   type_of_out='prime'))
    print('Prime:', even_odd_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print('Fibonacci ->', fibonacci(8))
