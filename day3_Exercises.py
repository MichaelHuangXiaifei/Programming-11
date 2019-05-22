#question 1
def rightJustify(s):
    print(" " * (70 - len(s)) + s)

rightJustify("allen")

#question 2
def grild():
    print("+ - - - - + - - - - +")
    for i in range(4):
        print("|         |         |")
    print("+ - - - - + - - - - +")
    for i in range(4):
        print("|         |         |")
    print("+ - - - - + - - - - +")

grild()

#question 3
def doFour(f):
    doTwice(f)
    doTwice(f)

def doTwice(f):
    f()
    f()

def printSpam():
    print("spam")

doFour(printSpam)