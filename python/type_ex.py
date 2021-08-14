"""type() about."""

###### type() for builtin types

x = 'Hello World'
print(type(x))

x = 69
print(type(x))

x = 3.14159
print(type(x))

x = 3 + 2j
print(type(x))

x = ['apple', 'banana', 'mango']
print(type(x))

x = ('apple', 'banana', 'mango')
print(type(x))

x = range(6)
print(type(x))

x = {'a': 65, 'b': 66}
print(type(x))

x = {'apple', 'banana', 'mango'}
print(type(x))

x = frozenset({'apple', 'banana', 'mango'})
print(type(x))

x = True
print(type(x))

x = b'mango juice'
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

print()

###### type() for user defined datatype

class Fruit:
    def __init__(self, name):
        self.name = name

x = Fruit('banana')
print(type(x))
print()

###### type of type object

x = 12
print(type(type(x)))
print()

######
