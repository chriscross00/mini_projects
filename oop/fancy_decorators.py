class Circle:

    def __init__(self, radius):
        self._radius = radius

    #@property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return self.pi() * self.radius**2

    @staticmethod
    def pi():
        return 3.1415926535
