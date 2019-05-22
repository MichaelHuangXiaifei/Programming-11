import math
# day 3 functions:


def square_root_of_ten():
    return math.sqrt(10)


def a_number_plus_the_square_root_of_ten(a_number):
    return a_number + square_root_of_ten()


# day 4 recursion:
t = 0


def ten_times(input_words):
    global t
    if t < 10:
        print(input_words)
        t += 1
        ten_times(input_words)
    else:
        pass


ten_times(input())
del t

# day 5 fruitful functions and more recursion:
t = 1
accumulator = 0


def summation_from_1(input_number):
    global t
    global accumulator
    if t <= input_number:
        accumulator += t
        t += 1
        return summation_from_1(input_number)
    else:
        return accumulator


print(summation_from_1(100))
del t
del accumulator

# day 6 iteration
number = float(input())
count = 0

while number > 1.1:
    number = math.sqrt(number)
    count += 1

print(count)

# day 7 string


def judgement_upper_lower_cases(word):
    count_capital = 0
    count_lower = 0
    for i in word:
        if i.isupper():
            count_capital += 1
        if i.islower():
            count_lower += 1
    print("there are", count_capital, "capital letter(s)")
    print("there are", count_lower, "lowercase letter(s)")


judgement_upper_lower_cases("banana")
