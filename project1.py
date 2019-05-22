# simplified version of the game blackjack

import random  # import the module "Random"

# define values for player and computer
valueOfPlayer = random.randint(1, 14)
valueOfComputer = random.randint(1, 28)

# show the start value to player
print("You start at", valueOfPlayer)


while 1:  # keep running following lines until the player's value is bigger than 28, or answer is "NO"
    answer = input('Do you want another one? '
                   '(answer "Yes" or "No")\n')  # ask the player if they want's to add another value
    if answer == "Yes":  # if the answer from player is "Yes"
        valueOfPlayer = valueOfPlayer + random.randint(1, 14)  # add another value
        if valueOfPlayer > 28:  # if the value of player is bigger than 28
            print("You now have ", valueOfPlayer, ", busted", sep="")  # the player loose
            exit()
        elif valueOfPlayer <= 28:  # if player's value is smaller than 28
            print("Now you have", valueOfPlayer)  # show the value to player
    elif answer == "No":  # is the player don't wants to add another value
        break  # stop the loop
    else:
        print("Please give me a proper answer!")

# compare the result
if valueOfPlayer == valueOfComputer:
    print("You have ", valueOfPlayer, " and the computer has ", valueOfComputer, ", it’s a draw", sep="")  # draw
    exit()
elif valueOfPlayer > valueOfComputer:
    print("You have ", valueOfPlayer, " and the computer has ", valueOfComputer, ", you win", sep="")  # win
    exit()
elif valueOfPlayer < valueOfComputer:
    print("You have ", valueOfPlayer, " and the computer has ", valueOfComputer, ", you lose", sep="")  # loose
    exit()
