import functools
import time

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        # Actions before function
        value = func(*args,**kwargs)
        # Actions after function
        return value
    return wrapper_decorator

def debug(func):
    '''Print the function signature and return the value'''
    @functools.wraps(func)
    def wrapper_debug(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}= {v!r}" for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args,**kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper_debug

def slow_down(func):
    '''Sleep 1 second before calling the function'''
    @functools.wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(1)
        value = func(*args,**kwargs)
        return value
    return wrapper_slow_down