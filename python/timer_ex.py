"""Atempt to change time alltoghether."""

class Time(object):
    """Time for a day, attrs: hour, min, sec."""
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.secon + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum
