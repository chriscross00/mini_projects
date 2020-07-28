from fancy_decorators import Circle
import class_decorators

def main():
    # c1 = Circle(5)
    # print(c1.area)
    # c1.radius = 0
    # print(c1.area)
    # cd = class_decorators.learn_class()

    print(class_decorators.learn_class.class_method())
    print(class_decorators.learn_class.static_method())
    print(class_decorators.learn_class.method())

if __name__ == '__main__':
    print("startup message")
    main()
