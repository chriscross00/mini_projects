# https://realpython.com/instance-class-and-static-methods-demystified/

class learn_class:
    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'
