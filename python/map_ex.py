"""map() about."""

def square(n):
    return n**2

x = map(square, [1, 2, 3, 4, 5, 6])
print(list(x))

###### map() with lambda function

x = map(lambda n: n**2, [1, 2, 3, 4, 5, 6])
print(list(x))

######
