# oop
import math


class Point:
    """Represents a point. attributes: x coordinate, y coordinate. """

    x = float()
    y = float()

    def move(self, x, y):
        self.x += x
        self.y += y

    def set_coordinate(self, x, y):
        x_dif = x - self.x
        y_dif = y - self.y
        self.move(x_dif, y_dif)

    def __str__(self):
        return '%s, %s' % (self.x, self.y)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Diatance:
    """Represents a distance. attributes: point 1, point 2. """

    d = float()

    def measure(self, point1, point2):
        self.d = math.sqrt((point2.y - point1.y) ** 2 + (point2.x - point1.x) ** 2)


class Rectangle:
    """Represents a rectangle. attributes: the lower left corner, length, width. """
    corner = Point()
    length = float()
    width = float()

    def area(self):
        return self.length * self.width

    def __init__(self, corner=Point(0, 0), length=0, width=0):
        self.corner = corner
        self.length = length
        self.width = width


class Circle:
    """Represents a circle. attributes: center point, radius. """

    def __init__(self, center=Point(0, 0), r=0):
        self.center = center
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def increase_area(self, area):
        r2 = math.sqrt((area + math.pi * self.r ** 2) / math.pi)
        self.r = r2

    def multiply_area(self, times):
        self.r *= math.sqrt(times)

class Time:
    """Represents the time of day. attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


def is_after(t1, t2):
    t1_s = t1.hour * 3600 + t1.minute * 60 + t1.second
    t2_s = t2.hour * 3600 + t2.minute * 60 + t2.second


time0 = Time(10, 1, 2)
print(time0)
