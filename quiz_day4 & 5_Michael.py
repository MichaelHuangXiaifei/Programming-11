import time
# question 1


def sum_calculation(n, final_value):
    if n <= 0:
        print(final_value)
    else:
        final_value = final_value + n
        sum_calculation(n - 2, final_value)


sum_calculation(100, 0)  # the second parameter should always be zero

# question 2


def count_down(input_from_user, count_times):
    if count_times <= input_from_user:
        time.sleep(1)
        print(count_times)
        count_times = count_times + 1
        count_down(input_from_user, count_times)
    elif count_times > input_from_user:
        print("Time is up!")


count_down(int(input("Input a number\n")), 1)


def count_down1():
        time.sleep(1)
        print(time.strftime("%Y.%m.%d, %H:%M:%S", time.localtime(time.time())))
        count_down1()


count_down1()
