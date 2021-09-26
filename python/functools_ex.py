"""functools about."""

#1 reduce() iterate over each item in a list and return a single value

from functools import reduce

def add_num(a, b):
    return a + b
a = [ 1, 2, 3, 10]
print(reduce(add_num, a))
print()

### format a list of strings using the reduce()

from functools import reduce
def add_str(a,b):
    return a+' '+b
a = ['MUO', 'is', 'a', 'media', 'website']
print(reduce(add_str, a))
print()

######2 split()

words = "column1 column2 column3"
words = words.split(" ")
print(words)
print()

######3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
    print(i, j)
print()

###3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
    print(i, j)
print()

###3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):   # ...enumerate(fruits, start=1): - not from 0
    print(i, j)
print()

### standard?

fruits = ["grape", "apple", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])
print()

######
