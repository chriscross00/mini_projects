from decorators import timer
from fancy_decorators import Circle


@timer
def waste_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])


def main():
    c1 = Circle(5)
    print(c1.radius())
    print(c1.__dict__)

if __name__ == '__main__':
    print("startup message")
    main()
