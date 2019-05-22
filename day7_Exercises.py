# 7.1
count = 0
for i in "banana":
    if i == "a" or i == "A":
        count = count + 1
print(count)

# 7.2


def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("banana", "a", 0))

# 7.3
word = input("word: ")


def is_palindrome(input_word):
    if input_word == input_word[::-1]:
        return True
    else:
        return False


print(is_palindrome(word))

# 7.4
# the function any_lowercase4 actually does

# 7.5


def rotate_word(original_word, rotation_coefficient):
    finalWord = ''
    for i in original_word:
        numericCode = ord(i)
        if i.islower():
            if rotation_coefficient > 0:
                for rotationTimes in range(rotation_coefficient % 27):
                    if numericCode < 122:
                        numericCode = numericCode + 1
                    elif numericCode == 122:
                        numericCode = 97
            if rotation_coefficient < 0:
                for rotationTimes in range(abs(rotation_coefficient) % 27):
                    if numericCode > 97:
                        numericCode = numericCode - 1
                    elif numericCode == 97:
                        numericCode = 122
        if i.isupper():
            if rotation_coefficient > 0:
                for rotationTimes in range(rotation_coefficient % 27):
                    if numericCode < 90:
                        numericCode = numericCode + 1
                    elif numericCode == 90:
                        numericCode = 65
            if rotation_coefficient < 0:
                for rotationTimes in range(abs(rotation_coefficient % 27)):
                    if numericCode > 65:
                        numericCode = numericCode - 1
                    elif numericCode == 65:
                        numericCode = 90
        finalWord = finalWord + chr(numericCode)
    return finalWord


print(rotate_word("HAL", 1))


def another_way_to_rotate_word(word, rotation_coefficient):
    result = ''
    for i in word:
        if i.islower():
            result += chr(((ord(i) + rotation_coefficient % 27) % 123 % 97) + 97)
        if i.isupper():
            result += chr(((ord(i) + rotation_coefficient % 27) % 91 % 65) + 65)
    return result


print(another_way_to_rotate_word('HAL', 100))
