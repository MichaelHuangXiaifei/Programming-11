#Before spring festival
'''
import math
def showLyrics(sentence1,sentence2):
    #print("I'm a lumberjack, and I'm okay.")
    #print("I sleep all night and I work all day.")
    print(sentence1)
    print(sentence2)

showLyrics("I'm a lumberjack, and I'm okay.",
           "I sleep all night and I work all day.")
print(type(showLyrics))
'''

#After spring festival
'''
import math
print(math.pi)
print(math.sin(1 / (6 * math.pi)))
'''

def repeat(things,times):
    a = 0
    while a < times:
        print(things,end="\n")
        a = a + 1

repeat(1,0)

#anotner day of day 3
list1 = [1,2]
list2 = [3,4]

def vertical(x,y):
    third = 0
    third = x
    x = y
    y = third
    return [x,y]
