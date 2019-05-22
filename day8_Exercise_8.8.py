import time
start_time = time.time()
# 8.8

# using append method:


def build_list():
    fin = open('words.txt')
    new_list = []
    for a in fin:
        word = a.strip()
        new_list.append(word)
    return new_list


vocabularyList = build_list()
# print(vocabularyList)
print("--- %s second ---" % (time.time() - start_time))

start_time = time.time()
# using self increment method:


def build_list():
    fin = open('words.txt')
    new_list = []
    for a in fin:
        word = a.strip()
        new_list += [word]
    return new_list


vocabularyList = build_list()
# print(vocabularyList)
print("--- %s second ---" % (time.time() - start_time))
