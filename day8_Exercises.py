import time
# 8.1
print('8.1:')
t = [[1, 2], [3], [4, 5, 6]]


def nested_sum(nested_list):
    summation = 0
    for outer_item in nested_list:
        for inner_item in outer_item:
            summation += inner_item
    return summation


print(nested_sum(t))

# 8.2
print('8.2')
t = [1, 2, 3]


def cumsum(original_list):
    index = 0
    new_list = []
    for i in original_list:
        if index == 0:
            new_list.append(i)
            index += 1
        else:
            new_list.append(i + new_list[index - 1])
            index += 1
    return new_list


print(cumsum(t))

# 8.2 with out using append method
print('8.2 with out using append method')
t = [1, 2, 3]


def cumsum(original_list):
    for i in range(1, len(original_list)):
        original_list[i] = original_list[i - 1] + original_list[i]
    return original_list


print(cumsum(t))

# 8.3
print('8.3')
t = [1, 2, 3, 4]


def middle(original_list):
    new_list = []
    for i in original_list[1:-1]:
        new_list.append(i)
    return new_list


print(middle(t))

# 8.4
print('8.4')
t = [1, 2, 3, 4]


def chop(list_name):
    del list_name[0]
    del list_name[-1]


chop(t)
print(t)

# 8.5
print('8.5')


def is_sorted(input_list):
    for i in range(1, len(input_list)):
        if str(input_list[i]) < str(input_list[i - 1]):
            return False
    return True


print(is_sorted([1, 2, 3]))

# 8.6 wrong answer
# print('8.6')
#
#
# def is_anagram(word1, word2):
#     for i in word1:
#         if i not in word2:
#             return False
#     for i in word2:
#         if i not in word1:
#             return False
#     count1 = 0
#     count2 = 0
#     for compare_1 in word1:
#         for compare_2 in word1:
#             if compare_1 == compare_2:
#                 count1 += 1
#     for compare_1 in word2:
#         for compare_2 in word2:
#             if compare_1 == compare_2:
#                 count2 += 1
#     if count1 != count2:
#         return False
#     return True
#
#
# print(is_anagram("aab", "bba"))

# 8.6
print('8.6')


def is_anagram(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)
    for i in word1_list:
        if i in word2_list:
            del word2_list[word2_list.index(i)]
    if len(word2_list) == 0:
        return True
    return False


print(is_anagram("aab", "bba"))
time.sleep(10)
# 8.7
print('8.7')


def has_duplicates(original_list):
    for element in original_list:
        count = 0
        for check in original_list:
            if check == element:
                count += 1
        if count >= 2:
            return True
    return False


print(has_duplicates(['b', 'a', 'n']))
print(has_duplicates(['b', 'a', 'n', 'a', 'n', 'a']))

# 8.8

# using append method:
start_time = time.time()


def build_list():
    fin = open('words.txt')
    new_list = []
    for a in fin:
        word = a.strip()
        new_list.append(word)
    return new_list


vocabularyList = build_list()
print(vocabularyList)
print("--- %s second ---" % (time.time() - start_time))

# using self increment method:
start_time = time.time()


def build_list():
    fin = open('words.txt')
    new_list = []
    for a in fin:
        word = a.strip()
        new_list += [word]
    return new_list


vocabularyList = build_list()
print(vocabularyList)
print("--- %s second ---" % (time.time() - start_time))

# 8.9
print('8.9')


def in_bisect(target_list, val):
    start = 0
    end = len(target_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target_list[mid] == val:
            return mid
        elif target_list[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return


print(in_bisect(vocabularyList, 'high'))

# 8.10
print('8.10')

for first_word in vocabularyList:
    for second_word in vocabularyList:
        if first_word == second_word[::-1]:
            print(first_word, second_word)

# 8.11
print('8.11')


# .1
def interlocked_words():
    fin = open('words.txt')
    for a in fin:
        word = a.strip()
        i = 0
        word1 = ''
        while i < len(word):
            word1 += word[i]
            i += 2
        i = 1
        word2 = ''
        while i < len(word):
            word2 += word[i]
            i += 2
        if in_bisect(vocabularyList, word1) is not None and in_bisect(vocabularyList, word2) is not None:
            print(word, word1, word2)


interlocked_words()


# .2
def three_way_interlocked_words():
    fin = open('words.txt')
    for a in fin:
        word = a.strip()
        i = 0
        word1 = ''
        while i < len(word):
            word1 += word[i]
            i += 3
        i = 1
        word2 = ''
        while i < len(word):
            word2 += word[i]
            i += 3
        word3 = ''
        while i < len(word):
            word3 += word[i]
            i += 3
        if in_bisect(vocabularyList, word1) is not None and\
                in_bisect(vocabularyList, word2) is not None and \
                in_bisect(vocabularyList, word3) is not None:
            print(word, word1, word2, word3)


three_way_interlocked_words()
