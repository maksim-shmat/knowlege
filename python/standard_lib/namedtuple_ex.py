"""Underclass tuple with named fields."""

#1

bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'female')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))

'''RESULTS:
Representation: ('Bob', 30, 'male')

Field by index: Jane

Fields by index:
Bob is a 30 year old male
Jane is a 29 year old female
'''

#2 namedtuple person

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nField by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

'''RESULTS:
Representation: Person(name='Bob', age=30)

Field by name: Jane

Field by index:
Bob is 30 years old
Jane is 29 years old
'''

#3 namedtuple ._fields

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)

'''RESULTS:
Representation: Person(name='Bob', age=30)
Fields: ('name', 'age')
'''

#4 namedtuple asdict

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('As Dictionary:', bob._asdict())

'''RESULTS:
Representation: Person(name='Bob', age=30)
As Dictionary: {'name': 'Bob', 'age': 30}
'''

#5 namedtuple replace

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)

'''RESULTS:
Before: Person(name='Bob', age=30)
After: Person(name='Robert', age=30)
Same?: False
'''

#6 Two simple dict abc and cba is equal, but two ordered dict abc and cba not.

import collections

print()
print('dict:', end=' ')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print(d1 == d2)
print('OrderedDict:', end=' ')
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print(d1 == d2)

'''RESULTS:
dict: True
OrederedDict: False
'''

#7 OrderedDict move to end elements

import collections

d = collections.OrderedDict(
        [('a', 'A'), ('b', 'B'), ('c', 'C')]
)
print('Before:')
for k, v in d.items():
    print(k, v)

d.move_to_end('b')

print('\nmove_to_end():')
for k, v in d.items():
    print(k, v)

d.move_to_end('b', last=False)

print('\nmove_to_end(last=False):')
for k, v in d.items():
    print(k, v)

'''RESULTS:
Before:
a A
b B
c C

move_to_end():  # move key 'b' to end of OrderedDict
a A
c C
b B

move_to_end(last=False):  # move key 'b' ot start of OrderedDict
b B
a A
c C
'''
