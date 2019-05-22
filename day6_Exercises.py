# 6.1
import math
import random


def my_sqrt(number, estimate):
    for i in range(10):
        estimate = (estimate + (number / estimate)) / 2
    return estimate


print("a", " " * 3, "mysqrt(a)", " " * 5, "math.sqrt(a)", " " * 2, "diff", sep='')
print("-", " " * 3, "---------", " " * 5, "------------", " " * 2, "----", sep='')
for i in range(9):
    a = i + 1
    mySqrt = round(my_sqrt(a, random.randint(1, 9)), 11)
    mathSqrt = round(math.sqrt(a), 11)
    diff = my_sqrt(a, random.randint(1, 9)) - math.sqrt(a)  # abs(mySqrt - mathSqrt)
    print(round(float(a), 1), " ",
          mySqrt, " " * (13 - len(str(mySqrt))),
          " ", mathSqrt,
          " " * (13 - len(str(mathSqrt))),
          " ", diff, sep='')

# 6.2


def eval_loop():
    while True:
        answer = input("Input an mathematical expression\n")
        if answer == "done":
            break
        elif answer == '':
            continue
        else:
            print(eval(answer))


eval_loop()

# 7.3


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def estimate_pi():
    reciprocal_pi = ((2 * math.sqrt(2)) / 9801)
    summation_of_rest = 0
    i = 0
    while True:
        if (factorial(4 * i) * (1103 + 26390 * i)) / (factorial(i) ** 4 * 396 ** (4 * i)) < 10 ** -15:
            break
        else:
            summation_of_rest = summation_of_rest + (factorial(4 * i) * (1103 + 26390 * i)) / (factorial(i) ** 4 * 396 ** (4 * i))
            i = i + 1
    reciprocal_pi = reciprocal_pi * summation_of_rest
    return reciprocal_pi ** -1


print(estimate_pi())
