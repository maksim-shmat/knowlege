"""Add a cache to any function."""

def fib(x):
    if x <= 1:
        return 1
    return fib(x -1) + fib(x)

###

from functools import cache

@cache
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 1) + fib(x)

###

from functools import lru_cache

@lru_cache
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 1) + fib(x)

### maximum size of 1000 elements

from functools import lru_cache

@lru_cache(max_size=1000)
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 1) + fib(x)
