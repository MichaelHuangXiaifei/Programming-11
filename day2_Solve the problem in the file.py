#Question 1
print("Question 1: ")
#Define variable width
width = 17
#Define variable height
height = 12.0
#Define variable delimiter
delimiter = "."

#Value of width/2
print(width / 2)
#Type of width/2
print(type(width / 2))
#Value of width/2.0
print(width / 2.0)
#Type of width/2.0
print(type(width / 2.0))
#Value of height/3
print(height / 3)
#Type of heigh/3
print(type(height / 3))
#Value of 1+2+5
print(1 + 2 * 5)
#Type of 1+2+5
print(type(1 + 2 * 5))
#Value of delimiter*5
print(delimiter * 5)
#Type of delimiter*5
print(type(delimiter * 5))

#Question 2
print("Question 2: ")
#to import pi function
import math
#Question a
print("The volume of a sphere with radius 5 is",round((3 / 4) * math.pi * (5 ** 3),2))
#Question b
print("The total price wholesale cost for 60 copies is ",round(24.95 * 0.6 * 60 + 3 + 59 * 0.75,2),"$",sep="")
#Question c
print("He will get home for breakfast at ",int(int((6 * 60 + 52) + 8.25 + 3 * 7.2 + 8.25) / 60),
      ":",int((6 * 60 + 52) + 8.25 + 3 * 7.2 + 8.25) % 60,sep="")
