# iteration

for i in range(10):
    print(i + 1)

# kinds of repetition


def countdown(times):
    i = times
    while i > 0:
        print(i)
        i = i - 1
    print("Blastoff!")


def anti_countdown(times):
    i = 1
    while i <= times:
        print(i)
        i = i + 1
    print("Time is up!")


anti_countdown(10)

# use condition to stop the loop
'''
while True:
    if input("take a guess of what I am thinking\n") == "asdf":
        print("Right!")
        break
    else:
        print("Wrong!")
'''

# Another example of while statement using square roots


def square_root(number, estimate):
    for i in range(10):
        estimate = (estimate + (number / estimate)) / 2
    print(estimate)


square_root(int(input("What is the number that "
                      "you want to calculate "
                      "the square root of?\n"))
            ,
            int(input("What is your first guess?\n")))
