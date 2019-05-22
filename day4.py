# name = input("What is your name?\n")
# print("I got it, your name is ",name,".",sep="")
#
# def equivalentToInput(prompt):
#     return input(prompt)
#
# name = equivalentToInput("What is your name?\n")
# print("I got it, your name is ",name,".",sep="")

# print(5 == 5)

# A question from math
import random

possibleAnswer = 0
for i in range(-4, 5):
    a = i
    for m in range(-4, 5):
        b = m
        if abs(a) + abs(b) == 4:
            print(a, ", ", b, sep="")
            possibleAnswer = possibleAnswer + 1

print("There are", possibleAnswer, "possible answers.")

# Conditional execution
x = int(input("What is x\n"))
if x > 0:
    print("X is positive")

if x < 0:
    print("X is negative")

if x == 0:
    print("X is equal to 0")

if x % 2 == 0:
    print("X is even")

if x % 2 != 0:
    print("X is odd")

# mini game
y = random.randint(0, 500)

for i in range(11):
    if i == 10:
        print("no more chances!")
        break
    print(" " * 134, "You have ", 10 - i, " chance left.", sep="")
    x = int(input("Take a guess from 0 to 500\n"))
    if x > y:
        print("It's too big!")
    elif x < y:
        print("It's too small!")
    elif x == y:
        print("That's it!")
        break

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
    elif n == 0:
        print("Fire!")

countdown(20)