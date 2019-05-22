# midterm

# 19


def stop_when_is_10():
    while True:
        answer = float(input())
        if answer == 10:
            break


stop_when_is_10()

# 20


def print_x_times(word):
    for i in range(len(word)):
        print(word)


print_x_times("apple")

# 21


def find_shorter_in_longer(longer_input, shorter_input):
    return longer_input.find(shorter_input), longer_input.find(shorter_input) + len(shorter_input) - 1


print(find_shorter_in_longer("aiw", "i"))

# 22

lines = int(input())
answer = ''
answer_list = []

for i in range(lines):
    input_message = input()
    list_input_message = input_message.split(" ")
    for a in range(int(list_input_message[0])):
        answer += list_input_message[1]
    answer_list.append(answer)
    answer = ''

for i in range(len(answer_list)):
    print(answer_list[i])
