# https://realpython.com/instance-class-and-static-methods-demystified/

class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        return self.area * height

    @classmethod
    def unit_circle(cls):
        return cls(1)

    @staticmethod
    def pi():
        return 3.1415926535
