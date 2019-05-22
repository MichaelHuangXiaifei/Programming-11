# 10
def ask_massage_and_display(message, times_to_display):
    for i in range(times_to_display):
        print(message)


ask_massage_and_display(input("Input your message: "), int(input("How many times do you want to repeat?\n")))

# 11


def get_length(word):
    length = 0
    for i in word:
        length += 1
    return length


print(get_length("banana"))
