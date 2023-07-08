"""yield about."""

#1 gen yield for

def print_squares(start, end):
    for n  in range(start, end):
        yield n ** 2

    for n in print_squares(2, 5):
        print(n)

# RESULTS:
# 4, 9, 16

#2 gen yield from

def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)

# RESULTS:
# 4, 9, 16

#3
