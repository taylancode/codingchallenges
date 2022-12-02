from functools import wraps
from time import time

class Decorators:

    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
            Function:
                - Decorator that can be added to any function to time it
            Params:
                - Takes the function and all its argument
            Returns:
                - Called function and its args
            '''
            start = time()
            result = func(*args, **kwargs)
            end = time()
            print('Function: %r took: %.4f ms' % (func.__name__, (end-start)*1000))
            return result
        return wrapper