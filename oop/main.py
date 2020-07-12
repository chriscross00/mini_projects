from decorators import do_twice

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


def main():
    foo = return_greeting("your_name_here")
    print(foo)

if __name__ == '__main__':
    print("startup message")

    main()
