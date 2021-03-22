""" Little bit examples python/django about."""

###### Iterables

class Fibonacci(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        a, b = 0, 1
        for x in range(self.count):
            if x < 2:
                yield x
            else:
                c = a + b
                yield c
                a, b = b, c

for x in Fibonacci(5):
    print(x)

for x in Fibonacci(10):
    print(x)

######
