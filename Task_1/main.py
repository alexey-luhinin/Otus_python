import time
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
