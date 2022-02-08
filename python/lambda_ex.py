"""Lambda function about."""

square = lambda a: a*a
# call lambda function
result = square(6)
print(result)
print()

###### multiple arguments

mul = lambda a,b: a*b
# call lamda function
result = mul(5,3)
print(result)
print()

###### with no arguments

six = lambda : 6
# call lambda function
result = six()
print(result)
print()

###### recursive lambda function

factorial = lambda a: a*factorial(a-1) if (a>1) else 1
# call lambda function
result = factorial(5)
print(result)
print()

###### return lambda function

import math
# function returning lambda function
def myfunc(n):
    return lambda a : math.pow(a, n)

# lambda functions
square = myfunc(2)  # square = lambda a : math.pow(a, 2)
cube = myfunc(3) # cube = lambda a: math.pow(a, 3)
squareroot = myfunc(0.5) # squareroot = lambda a : math.pow(a, 0.5)

print(square(3))
print(cube(3))
print(squareroot(3))
print()

###### lambda function with if Else Condition

x = lambda n: n**2 if n%2 == 0 else n**3

print(x(4))
print(x(3))
print()

###### lambda function with nested if else condition

x = lambda n: n if n%10 == 0 else (n**2 if n%2 == 0 else n**3)

print(x(4))
print(x(3))
print(x(10))
print()

#1 Sum of all the numbers in a sequence

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
joh = reduce(lambda x, y: x + y, numbers)
print(joh)  # 1161

#2
