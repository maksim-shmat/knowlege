"""map() about."""

def square(n):
    return n**2

x = map(square, [1, 2, 3, 4, 5, 6])
print(list(x))
# [1, 4, 9, 16, 25, 36]

#1 map() with lambda function

x = map(lambda n: n**2, [1, 2, 3, 4, 5, 6])
print(list(x))
# [1, 4, 9, 16, 25, 36]

#2 

fur = list(map(str, range(10)))  # Equivalent to [str(i) for i in range(10)]
print(fur)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#3

