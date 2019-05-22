# 5.2


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))

# 5.3


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome_using_loop_method(word):
    while len(word) > 1:
        if first(word) == last(word):
            word = middle(word)
        else:
            return False
    return True


print(is_palindrome_using_loop_method(input()))

# 5.4


def is_power(a, b):
    if a % b == 0 and a > b:
        return is_power(a / b, b)
    elif a == b:
        return True
    else:
        return False


print(is_power(1024, 2))

# 5.5


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(125, 15))
