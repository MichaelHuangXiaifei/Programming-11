class Time:
    """Represent a time object. Attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%d:%d:%d" % (self.hour, self.minute, self.second)


time0 = Time(25, 30, 2)
# 11.1


def mul_time(time, number):
    total_second = time.hour * 3600 + time.minute * 60 + time.second
    total_second *= number
    hour = total_second / 3600
    minute = total_second % 3600 / 60
    second = total_second % 60
    return Time(hour, minute, second)


print(mul_time(time0, 2))


# 11.2
def average_pace(finishing_time, distance):
    total_second = finishing_time.hour * 3600 + finishing_time.minute * 60 + finishing_time.second
    total_second /= distance
    hour = total_second / 3600
    minute = total_second % 3600 / 60
    second = total_second % 60
    return Time(hour, minute, second)


print(average_pace(time0, 2))
