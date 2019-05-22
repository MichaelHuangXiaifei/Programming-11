# day 9 Dictionaries

# 9.1 A dictionary is a mapping
eng2sp = dict()
print(eng2sp)

eng2sp["one"] = "uno"
print(eng2sp)

eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
print(eng2sp)

print(eng2sp["two"])
print(len(eng2sp))

for i in eng2sp:
    print(i)


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("value is not in the dictionary")


letters_count = dict()
for i in "python is not a snake":
    if i != ' ':
        if i in letters_count:
            letters_count[i] += 1
        else:
            letters_count[i] = 1

print(letters_count)

invert_letters_count = dict()
for letter in letters_count:
    val = letters_count[letter]
    invert_letters_count.setdefault(val, list()).append(letter)
#    invert_letters_count[val].append(letter)

print(invert_letters_count)
