# day 7 Strings
# 7.1 A string is a sequence
fruit = "banana"
for i in range(6):
    letter = fruit[i]
    print(letter, end='')
# 7.2 len method
last = fruit[len(fruit) - 1]
print("\n", last, sep='')
# 7.3
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'O' or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

print(fruit[1:3])
print("a" in "Banana")
print(fruit.upper())
print(fruit.find('a', 0, 5))

