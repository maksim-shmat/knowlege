"""Decorators factory about."""

from functools import wraps


def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                        'Result is too big({0}). Max allowed is {1}.'
                        .format(result, threshold))
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n ** 3

print(cube(5))

@max_result(100)
def square(n):
    return n ** 2
print(square(5))

@max_result(1000)
def multiply(a, b):
    return a * b
print(multiply(5, 2))

#RESULTS:


Result is too big(125). Max allowed is 75.
125
25
10
