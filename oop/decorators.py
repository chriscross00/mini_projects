# https://realpython.com/primer-on-python-decorators/

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice
