from functools import wraps


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
