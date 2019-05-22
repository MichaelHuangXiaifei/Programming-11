# lists

# 8.1 A list is a sequence
aSequenceOfNumber = [10, 20, 30, 40]
print(aSequenceOfNumber)

# 8.2 Lists are mutable
aSequenceOfNumber[0] = 20
print(aSequenceOfNumber)

# 8.3 Traversing a list
for i in aSequenceOfNumber:
    print(i)

# 8.4 List operations and slices

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

t = ["a", "b", "c", "d", "e", "f"]
print(t[1:3])
print(t[:4])
print(t[3:])
