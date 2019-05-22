# question 11
def printParagraph1():
    print("Twinkle,twinkle,little star,")
    print(" " * 7,"How I wonder what you are!",sep="")

def printParagraph2():
    print(" " * 15,"Up above the world so high,",sep="")
    print(" " * 15,"Like a diamond in the sky.",sep="")

def printParagraph3():
    print("Twinkle,twinkle,little star,")
    print(" " * 7, "How I wonder what you are", sep="")

printParagraph1()
printParagraph2()
printParagraph3()

# question 12
n = 1

def calculation(n):
    return n + (10 * n + n) + (100 * n + 10 * n + n)

print(calculation(n))

# question 13
import math
def rhombusCalculate(base,height):
    print("Your rhombus' area is ",base * height,".",sep="")
    print("Your rhombus' perimeter is ",2 * base + 2 * (height / math.sin(0.25)),".",sep="")

rhombusCalculate(1,2)

# Another way to solve question 12
n = 1
def calculation1(n):
    number1 = n
    number2 = int(str(n) + str(n))
    number3 = int(str(n) + str(n) + str(n))
    return number1 + number2 + number3

print(calculation1(n))
