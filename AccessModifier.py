import math

"""
    #(__) double underscore means private
    #(_) one underscore means protected
"""

class Circle:
    #(__) double underscore means private
    def __init__(self, radius):
        self.__radius = radius   # private variable

    def circumference(self):
        return 2 * math.pi * self.__radius

    def diameter(self):
        return self.__radius * 2

    def set_radius(self, radius):
        self.__radius = radius

    #(_) one underscore means protected
    def _get_radius(self):
        return self.__radius

    def show(self):
        print("Circle class")

    def __del__(self):
        pass


class Test:
    def show(self):
        print("Circle class")


class Sphere(Circle, Test):
    def __init__(self, radius):
        Circle.__init__(self, radius)
    def __init__(self, radius):
        super().__init__(radius)

    #override
    def circumference(self):
        return super().circumference()

    def volume(self):
        return (4/3) * math.pi *math.pow(self._get_radius(),3)


def start_code():
    circle = Circle(5)
    sphere = Sphere(6)

    print(circle._get_radius())
    print(sphere._get_radius())

    sphere.show()

    #precedence
    print(Sphere.mro())

if __name__ == "__main__":
    start_code()
