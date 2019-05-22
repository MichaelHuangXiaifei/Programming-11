import random
# Question 1
humanYear = int(input("Human's year input:\n"))
dogYear = 0

if humanYear < 0:
    pass
elif humanYear >= 0:
    if humanYear <= 2:
        dogYear = 10.5 * humanYear
    elif humanYear > 2:
        dogYear = 10.5 * 2 + (humanYear - 2) * 4
    print("Dog's age is", dogYear, "years old.")

# Question 2
threeSidesOfTriangle = input('Please input three side length of a triangle as "x, y, z" format.\n')
listOfThreeSideLength = threeSidesOfTriangle.split(", ")

lineA = int(listOfThreeSideLength[0])
lineB = int(listOfThreeSideLength[1])
lineC = int(listOfThreeSideLength[2])

if lineA + lineB > lineC and lineA + lineC > lineB and lineB + lineC > lineA:
    if lineA == lineB and lineB == lineC:
        print("Equilateral")
    elif lineA == lineB or lineA == lineC or lineB == lineC:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("It's not even a triangle!")

# Question 3
y = random.randint(1, 9)


def guess_from_1_to_9():
    x = int(input("Take a guess from 1 to 9\n"))
    if x > y:
        print("It's too big!")
        guess_from_1_to_9()
    elif x < y:
        print("It's too small!")
        guess_from_1_to_9()
    elif x == y:
        print("Well guessed!")


guess_from_1_to_9()

# Question 4
numberOne = 0
numberTwo = 1
fibonacciSequence = []


def fibonacci_sequence(number_one, number_two):
    if number_one < 50 and number_two < 50:
        if number_one < 50:
            fibonacciSequence.append(number_one)
            number_one += number_two
        if number_two < 50:
            fibonacciSequence.append(number_two)
            number_two += number_one
        fibonacci_sequence(number_one, number_two)


fibonacci_sequence(numberOne, numberTwo)

print(fibonacciSequence)

# Question 5


def iterates_from_1_to_50(i):
    if i >= 50:
        pass
    elif i < 50:
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            print(i + 1, ": FizzBuzz", sep="")
        elif (i + 1) % 3 == 0:
            print(i + 1, ": Fizz", sep="")
        elif (i + 1) % 5 == 0:
            print(i + 1, ": Buzz", sep="")
        i = i + 1
        iterates_from_1_to_50(i)


iterates_from_1_to_50(0)
