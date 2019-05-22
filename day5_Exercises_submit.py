# 5.3


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    if len(word) > 1:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False
    elif len(word) == 0 or len(word) == 1:
        return True


print(is_palindrome(input()))
