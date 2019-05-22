import math


class Point:
    """Represents a point in 2-D space. attributes: x coordinate, y coordinate. """

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


class Circle:
    """Represents a circle in 2-D space. attributes: center point, radius. """

    def __init__(self, point=Point(0, 0), r=0.0):
        self.center = point
        self.r = r

    def __str__(self):
        return 'a circle with center(%s) and radius %s' % (self.center, self.r)


class Rectangle:
    """Represents a rectangle in 2-D space. attributes: the lower left corner, width, height"""

    def __str__(self):
        return 'rectangle with lower left corner of(%s), ' \
               'width of %s, and height of %s' % (self.corner, self.width, self.height)

    def __init__(self, corner=Point(0, 0), width=0, height=0):
        self.corner = corner
        self.width = width
        self.height = height


def point_in_circle(circle, point):
    d = math.sqrt((point.y - circle.center.y) ** 2 +
                  (point.x - circle.center.x) ** 2)  # distance between point and circle center
    if d <= circle.r:
        return True
    else:
        return False


def rect_in_circle(rectangle, circle):
    point = rectangle.corner
    if point_in_circle(circle, point):
        point.move(0, rectangle.height)
        if point_in_circle(circle, point):
            point.move(rectangle.width, 0)
            if point_in_circle(circle, point):
                point.move(0, -rectangle.height)
                if point_in_circle(circle, point):
                    return True
    return False


# def rect_circle_overlap(rectangle, circle):
#     point = Point()
#     point.move(rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height)
#     if rectangle.corner.x < circle.center.x < point.x and \
#             rectangle.corner.y < circle.center.y < point.y:
#         return True
#     for x in range(rectangle.corner.x, rectangle.corner.x + rectangle.width + 1):
#         for y in range(rectangle.corner.y, rectangle.corner.y + rectangle.height + 1):
#             point.set_coordinate(x, y)
#             if point_in_circle(circle, point):
#                 return True
#     return False


def rect_circle_overlap(rectangle, circle):
    rectangle.corner.move(rectangle.corner.x - (- rectangle.width / 2), (- rectangle.height / 2))



circle0 = Circle(Point(5, 5), 0.1)
point0 = Point(200, 150)
rectangle0 = Rectangle(Point(0, 0), 10, 10)

print(point_in_circle(circle0, point0))
print(rect_in_circle(rectangle0, circle0))
print(rect_circle_overlap(rectangle0, circle0))
