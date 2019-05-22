# 1


def summation_dict(d):
    summation = 0
    for i in d:
        summation += d[i]


# 2

dict_with_duplicates = {'a': 1, 'b': 2, 'c': 1}


def remove_duplicates_dict(d):
    remove = list()
    for key1 in d:
        for key2 in d:
            if d[key1] == d[key2]:
                if key1 != key2:
                    remove.append(key2)
    for to_remove in remove:
        del d[to_remove]
    return d


print(remove_duplicates_dict(dict_with_duplicates))

# 3
need_sort_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}


def sort_dict_by_values(d):
    # inverse_d = dict()
    # for key in d:
    #     inverse_d.setdefault(d[key], []).append(key)
    # for value in inverse_d:
    key_list = list()
    for key in d:
        key_list.append(key)

    list_length = len(key_list)
    while list_length > 0:
        for i in range(list_length - 1):
            if d[key_list[i]] > d[key_list[i+1]]:
                key_list[i], key_list[i+1] = key_list[i+1], key_list[i]
        list_length -= 1
    return key_list


print(sort_dict_by_values(need_sort_dict))
