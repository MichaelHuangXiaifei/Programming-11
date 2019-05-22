# 1.
fin = open('words.txt')
for a in fin:  # traversing the word file
    word = a.strip()  # get the word and remove the line break
    if len(word) > 20:  # only print words that has more than 20 letters.
        print(word)

# 2.


def has_no_e():
    fin = open('words.txt')
    for a in fin:  # traversing the word file
        word = a.strip()  # get the word and remove the line break
        if not "e" in word or not "E" in word:  # do not print words that contain e or E
            print(word)


has_no_e()

# 3.


def uses_only(letters):
    fin = open('words.txt')
    for a in fin:  # traversing the word file
        word = a.strip()  # get the word and remove the line break
        if letters in word:  # check if the letter in parameter is in the word
            print(word)


uses_only("abc")

# 4.


def is_abecedarian():
    fin = open('words.txt')
    for a in fin:  # traversing the word file
        word = a.strip()  # get the word and remove the line break
        for i in range(len(word)):  # traversing the word
            if i + 1 < len(word):  # to prevent the error of index out of range
                if ord(word[i + 1]) < ord(word[i]):  # check numeric codes of the letter and one letter after
                    break
            if i + 1 == len(word):  # reach the end of word
                print(word)


is_abecedarian()
