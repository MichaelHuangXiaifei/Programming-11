#  quiz_dya 9_Michael

# 9.
n = 10
n_square = dict()

for i in range(1, n + 1):
    n_square[i] = i ** 2

print(n_square)

# 10.
t = {'a': 2, 'b': 3, 'c': 1, 'd': 5}
result = 1

for i in t:
    result *= t[i]

print(result)

# 11.
t = {'a': 2, 'b': 3, 'c': 1, 'd': 5}
t_val_list = list()

for i in t:
    t_val_list.append(t[i])

max_number = t_val_list[1]
for i in t_val_list:
    if i > max_number:
        max_number = i
print(max_number)

min_number = t_val_list[1]
for i in t_val_list:
    if i < min_number:
        min_number = i
print(min_number)

# 12
d1 = {'a': 2, 'b': 3, 'c': 4}
d2 = {'a': 1, 'b': 5, 'd': 4}
d3 = d2.copy()

for key1 in d1:
    if key1 in d3:
        d3[key1] += d1[key1]
    else:
        d3[key1] = d1[key1]

print(d3)
