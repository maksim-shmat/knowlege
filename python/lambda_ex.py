"""Lambda function about."""

square = lambda a: a*a
# call lambda function
result = square(6)
print(result)

###### multiple arguments

mul = lambda a,b: a*b
# call lamda function
result = mul(5,3)
print(result)

###### with no arguments

six = lambda : 6
# call lambda function
result = six()
print(result)

###### recursive lambda function

factorial = lambda a: a*factorial(a-1) if (a>1) else 1
# call lambda function
result = factorial(5)
print(result)

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

######
