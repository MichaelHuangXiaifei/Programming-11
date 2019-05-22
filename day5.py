# fruitful functions
# 5.1
import math


def area(radius):
    area = math.pi * radius**2
    return area


def perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter


print(round(area(5), 2))
print(round(perimeter(5), 2))


def absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
    elif x == 0:
        return x


print(absolute_value(0))


# 5.2
def distance(xc, yc, xp, yp):
    return math.sqrt((yp - yc) ** 2 + (xp - xc) ** 2)


def circle_area(r):
    return math.pi * r ** 2


print(round(circle_area(distance(1, 1, 2, 2)), 2))  # Des Cares coordinate system


# 5.3
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(is_divisible(9, 3))

# more about recursions
# try to calculate factorial using other ways
# definition of factorial: 0!=1，n!=(n-1)!×n


def factorial_my_solution(n):
    if n == 0:
        return 1
    else:
        return factorial_my_solution(n - 1) * n


print(factorial_my_solution(100))

# use recursion to calculate the term n of fibonacci sequence


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return "term number can't be zero"


print(fibonacci(100))
