"""itertools about."""

import itertools as it

# accumulate() - min(11), min(11,3), min(11, 3, 9)...
zacum = list(it.accumulate([11, 3, 9, 7, 5], func=min))
print(zacum)
print()

'''RESULTS:
[11, 3, 3, 3, 3]
'''

###### chain() glued several elements to one
# list(sorted(itertools.chain(*data)))
fchain = list(it.chain([1, 2, 3], [4, 5], [6]))
print(fchain)
print()

'''RESULTS:
[1, 2, 3, 4, 5, 6]
'''
###### combinations() - combinations and length of combinations

acombo = list(it.combinations([1, 2, 3], 2))
print(acombo)
print()

'''RESULTS:
[(1, 2), (1, 3), (2, 3)]
'''

###### clear elements, del it

from itertools import compress

letters = ['A', 'B', 'C', 'B', 'D']
mask = [1, 0, 1, 0, 0]  # 1 == True
result = compress(letters, mask)
print(list(result))

'''RESULTS:
['A', 'C']
'''

#1 chain

from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()

'''RESULTS:
1 2 3 a b c 
'''

#2 chain.from_iterable()

from itertools import *

def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
print()

'''RESULTS:
1 2 3 a b c
'''

#3 zip()

for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)

'''RESULTS:
(1, 'a')
(2, 'b')
(3, 'c')
'''

#4  zip_longest

from itertools import *

r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))

'''RESULTS:
zip stops early:
[(0, 0), (1, 1)]

zip_longest processes all of the values:
[(0, 0), (1, 1), (2, None)]

'''

#5  islice()

from itertools import *

print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')
print()
'''RESULTS:
Stop at 5:
0 1 2 3 4 

Start at 5, Stop at 10:
5 6 7 8 9 

By tens to 100:
0 10 20 30 40 50 60 70 80 90 
'''

#6 tee()

from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))
print()
'''RESULTS:
i1: [0, 1, 2, 3, 4]
i2: [0, 1, 2, 3, 4]
'''

#7 map()

def times_two(x):
    return 2 * x

def multiply(x, y):
    return (x, y, x * y)

print('Doubles:')

for i in map(times_two, range(5)):
    print(i)

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print('\nStopping:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)

'''RESULTS:
Doubles:
0
2
4
6
8

Multiples:
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36

Stopping:
(0, 0, 0)
(1, 1, 1)
'''

#8 starmap()

from itertools import *

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))

'''RESULTS:
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36
'''

#9
