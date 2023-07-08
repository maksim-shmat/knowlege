"""How many Fibonacci numbers do you want."""
'''
import math

fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#

fib = [0, 1]
num = int(input('How many Fibonacci numbers do you want?'))
for i in range(num -2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

# with def

def fibs1(num):
    result = [0, 1]
    for i in range(num -2):
        result.append(result[-2] + result[-1])
    return result

print(fibs1(10))
print(fibs1(15))
'''
#2 fibonacci first example

def fibonacci(N):
    """Return all fibonacci numbers up to N."""
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(50))

#RESULTS:

#[0]
#[0, 1, 1]
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#2 fibonacci second example

def fibonacci(N):
    """Return all fibonacci numbers up to N."""
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b

print(list(fibonacci(0)))
print(list(fibonacci(1)))
print(list(fibonacci(50)))

#3 fibonacci elegant

def fibonacci(N):
    """Return all fibonacci numbers up to N."""
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

print(list(fibonacci(0)))
print(list(fibonacci(1)))
print(list(fibonacci(50)))
