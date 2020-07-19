from decorators import timer


@timer
def waste_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])


def main():
    waste_time(6)

if __name__ == '__main__':
    print("startup message")

    main()
