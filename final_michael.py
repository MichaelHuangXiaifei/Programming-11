import random

# 22
letter_hist = dict()
original_list = ['a', 'b', 'c', 'a', 'b', 'a', 'c', 'b', 'c', 'a', 'd']
for letter in original_list:
    letter_hist[letter] = letter_hist.get(letter, 0) + 1
print(letter_hist)


# 23
class Name:
    """Represents names. Attributes: first name, lase name"""
    first_names = ['John', 'Jane', 'Bob', 'Lisa', 'Ashely']
    last_names = ['Smith', 'Doe', 'Trump', 'Lee', 'Dylan']

    def randomname(self):
        self.first_name = Name.first_names[random.randint(0, len(Name.first_names) - 1)]
        self.last_name = Name.last_names[random.randint(0, len(Name.last_names) - 1)]

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __init__(self):
        self.first_name = Name.first_names[0]
        self.last_name = Name.last_names[1]


n1 = Name()
n1.randomname()
print(n1)
