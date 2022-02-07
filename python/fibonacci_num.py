"""How many Fibonacci numbers do you want."""

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
