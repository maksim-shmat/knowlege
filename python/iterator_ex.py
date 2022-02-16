"""Iterators about."""

#1

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)  # 1597
        break

#2

it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2

#3 Making sequences form iterators

class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))

#3 
