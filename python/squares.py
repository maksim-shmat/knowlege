"""Simple task."""

# If you code like this you are not a Python dev!
squares = []
for n in range(10):
    squares.append(n ** 2)
print(squares)

#2 This is better, one line, nice and readable
squares2 = map(lambda n: n**2, range(10))

print(list(squares2))

# RESULTS:
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#3
a = [n ** 2 for n in range(10)]
print(a)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#4 using map and filter

sq1 = list(
        map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
)

# equivalent, but using list comprehensions

sq2 = [n ** 2 for n in range(10) if not n % 2]

print(sq1, sq1 == sq2)

#[0, 4, 16, 36, 64] True

#5
