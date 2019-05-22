# 11.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in original_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

# 12.


def find_long_words(sentence, length):
    long_word_list = []
    sentence_words_list = sentence.split(" ")
    for i in range(len(sentence_words_list)):
        sentence_words_list[i] = sentence_words_list[i].strip('`-=[]\;,./~!"@#$%\'^&*()_+{}|:<>?')
    for i in sentence_words_list:
        if len(i) > length:
            long_word_list.append(i)
    return long_word_list


print(find_long_words(input(), 5))

# test sentence: "This is not a perfect python program", and the words longer than 5 are "perfect python program"
