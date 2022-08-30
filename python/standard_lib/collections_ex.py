"""Collections lib about."""

# How many onesi repeat elements
from collections import Counter
a = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b', 'b', 'e', 'a']
cnt = Counter(a)
cnt.most_common(3)
print(cnt)
print()

#1 chainmap read

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))

'''RESULTS:
    Individual Values
a = A
b = B
c = C

Keys = ['b', 'c', 'a']
Values = ['B', 'C', 'A']

Items:
b = B
c = C
a = A

"d" in m: False
'''

#2 collections chainmap reorder

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# Reverse the list.
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

'''RESULTS:
    [{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
c = C

[{'b': 'B', 'c': 'D'}, {'a': 'A', 'c': 'C'}]
c = D
'''

#3 collections chainmap update behind

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))

'''RESULTS:
    Before: C
    After: E
'''

#4 chainmap update directly

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('a:', a)

'''RESULTS:
    Before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
After : ChainMap({'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})
a: {'a': 'A', 'c': 'E'}
'''

#5 chainmap new child

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)

'''RESULTS:
m1 before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m2 before: ChainMap({}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m1 after: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m2 after: ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
'''

#6 chainmap new child explicit

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))

# this code equivalent: m2 = collections.ChainMap(c, *m1.maps)
'''RESULTS:
m1["c"] = C
m2["c"] = E
'''
