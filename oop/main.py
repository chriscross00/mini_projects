from decorators import do_twice, a_dec

@do_twice
def whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"hello {name}")

@do_twice
def return_greeting(name):
    print("creating greeting")
    return f"hi {name}"

@a_dec
def first_func():
    """docstrings for the first function"""

    print("first function")

@a_dec
def second_func():
    """docstrings for the second function"""

    print("second function")

def main():
    print(first_func.__name__)
    print(first_func.__doc__)

    print(f"\n\n{second_func.__name__}\n{second_func.__doc__}")
    help(second_func)

if __name__ == '__main__':
    print("startup message")

    main()
