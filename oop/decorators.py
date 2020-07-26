# https://realpython.com/primer-on-python-decorators/
import functools
import time

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def a_dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        func()

    return wrapper

def timer(func):
    """print the runtime of the decorated function"""
    @functools.wraps(func)

    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"{func.__name__} ran in {run_time:.4f} secs")
        return value
    return wrapper_timer
