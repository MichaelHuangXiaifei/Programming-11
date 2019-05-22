# Question 4.1
import time
print(time.strftime("%H:%M:%S", time.localtime(time.time())), int(int(time.time()) / 60 / 60 / 24))

# Question 4.2


def check_fermat(a, b, c, n):
    if n < 2:
        print("n should be greater than 2")
    else:
        if a ** n + b ** n == c ** n:
            if a > 0 and b > 0 and c > 0:
                print("Holy smokes, Fermat was wrong!")
            else:
                print("No, that doesn't work.")
        elif a ** n + b ** n != c ** n:
            print("No, that doesn't work.")


check_fermat(int(input("a: ")), int(input("b: ")), int(input("c: ")), int(input("n: ")))

# Question 4.3


def is_triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        print("Yes")
    else:
        print("No")


def function_to_check_triangle(x, y, z):
    is_triangle(x, y, z)


function_to_check_triangle(int(input("x: \n")), int(input("y: \n")), int(input("z: \n")))

# Question 4.4


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)

# Question 4.5
'''

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


draw(1,1,1)
'''

