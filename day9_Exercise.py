# 9.1


def find_in_word_dict(word_input):
    word_dictionary = dict()
    file = open('words.txt')
    for word in file:
        word = word.strip()
        word_dictionary[word] = 0
    if word_input in word_dictionary:
        return True


print(find_in_word_dict("zymurgy"))

# 9.2


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, list())
        inverse[val].append(key)
    return inverse


print(invert_dict({'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 2, 'n': 3, 'i': 1, 's': 2, 'a': 2, 'k': 1, 'e': 1}))

# 9.3


def has_duplicates(original_list):
    letter_count = dict()
    for letter in original_list:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for letter in letter_count:
        if letter_count[letter] >= 2:
            return True
        else:
            continue
    return False


print(has_duplicates(['b', 'a', 'n']))
print(has_duplicates(['b', 'a', 'n', 'a', 'n', 'a']))

# 9.4


def rotate_word(word_to_rotate, rotation_coefficient):
    result = ''
    for i in word_to_rotate:
        if i.islower():
            result += chr(((ord(i) + rotation_coefficient % 27) % 123 % 97) + 97)
        if i.isupper():
            result += chr(((ord(i) + rotation_coefficient % 27) % 91 % 65) + 65)
    return result


rotate_pares = dict()
file = open("words.txt")
vocabulary_list = list()

for word in file:
    vocabulary_list.append(word)

for word1 in vocabulary_list:
    word1 = word1.strip()
    for rotate in range(1,26):
        for word2 in vocabulary_list:
            word2 = word2.strip()
            if rotate_word(word2, rotate) == word1:
                rotate_pares[word1] = word2
print(rotate_pares)
    