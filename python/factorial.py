"""factorial about."""

#1 return single value

def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result

f4 = factorial(5)  # f4 = 120
print(f4)

#2 with python batteries

from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)

f5 = factorial(5)  # f5 = 120
print(f5)

