"""Custom iterator about."""

#1

class OddEven:

    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) +
                list(range(1, len(data), 2)))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration

oddeven = OddEven('ThisIsCool!')
print(''.join(c for c in oddeven))  # TIICO!hssol

oddeven = OddEven('HoLa')  # or manually..
it = iter(oddeven)  # this calls oddeven.__iter__internally
print(next(it))  # H
print(next(it))  # L
print(next(it))  # o
print(next(it))  # a

TiICo!hssol
H
L
o
a
