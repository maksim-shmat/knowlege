"""functools about."""

#1 reduce() iterate over each item in a list and return a single value

from functools import reduce

def add_num(a, b):
    return a + b
a = [ 1, 2, 3, 10]
print(reduce(add_num, a))
print()

######2
