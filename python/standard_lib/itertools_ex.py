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

#9 count()

from itertools import *

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)

'''RESULTS:
(1, 'a')
(2, 'b')
(3, 'c')
'''

#10 count(start, step)

import fractions
from itertools import *

start = fractions.Fraction(1, 3)
step = fractions.Fraction(1, 3)

for i in zip(count(start, step), ['a', 'b', 'c']):
    print('{}: {}'.format(*i))

'''RESULTS:
1/3: a
2/3: b
1: c
'''

#11 cycle()

from itertools import *

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

'''RESULTS:
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'a')
(4, 'b')
(5, 'c')
(6, 'a')
'''

#12 repeat()

from itertools import *

for i in repeat('over-and-over', 5):
    print(i)

'''RESULTS:
over-and-over
over-and-over
over-and-over
over-and-over
over-and-over
'''

#13 repeat() and zip()

from itertools import *

for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)

'''RESULTS:
0 over-and-over
1 over-and-over
2 over-and-over
3 over-and-over
4 over-and-over
'''

#14 repeat and map()

from itertools import *

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))

'''RESULTS:
2 * 0 = 0
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
'''

#15 dropwhile()

from itertools import *

def should_drop(x):
    print('Testing:', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

'''RESULTS:
Testing: -1
Testing: 0
Testing: 1
Yielding: 1
Yielding: 2
Yielding: -2
'''

#16 takewhile()

from itertools import *

def should_take(x):
    print('Testing:', x)
    return x < 2

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

'''RESULTS:
Testing: -1
Yielding: -1
Testing: 0
Yielding: 0
Testing: 1
Yielding: 1
Testing: 2
'''

#17 filter()

from itertools import *

def check_item(x):
    print('Testing:', x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

'''RESULTS:
Testing: -1
Yielding: -1
Testing: 0
Yielding: 0
Testing: 1
Testing: 2
Testing: -2
Yielding: -2
'''

#18 filterfalse()

from itertools import *

def check_item(x):
    print('Testing:', x)
    return x < 1

for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
print()
'''RESULTS:
Testing: -1
Testing: 0
Testing: 1
Yielding: 1
Testing: 2
Yielding: 2
Testing: -2
'''

#19 compress()

from itertools import *

every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()

'''RESULTS:
3 6 9
'''

#20 groupby()

import functools
from itertools import *
import operator
import pprint

@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

# Make a set of data from 'Point' exemplars
data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))
print('Data:')
pprint.pprint(data, width=35)

# atempt group data by X value
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Sort data

data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Group sorted data by X value
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

'''RESULTS:
Data:
[(0, 0),
 (1, 1),
 (2, 2),
 (0, 3),
 (1, 4),
 (2, 5),
 (0, 6)]
Grouped, unsorted:
0 [(0, 0)]
1 [(1, 1)]
2 [(2, 2)]
0 [(0, 3)]
1 [(1, 4)]
2 [(2, 5)]
0 [(0, 6)]

Sorted:
[(0, 0),
 (0, 3),
 (0, 6),
 (1, 1),
 (1, 4),
 (2, 2),
 (2, 5)]

Grouped, sorted:
0 [(0, 0), (0, 3), (0, 6)]
1 [(1, 1), (1, 4)]
2 [(2, 2), (2, 5)]
'''

#21 accumulate()

from itertools import *

print(list(accumulate(range(5))))
print(list(accumulate('abcde')))

'''RESULTS:
[0, 1, 3, 6, 10]
['a', 'ab', 'abc', 'abcd', 'abcde']
'''

#22 custom accumulate()

from itertools import *

def f(a, b):
    print(a, b)
    return b + a + b

print(list(accumulate('abcde', f)))

'''RESULTS:
a b
bab c
cbabc d
dcbabcd e
['a', 'bab', 'cbabc', 'dcbabcd', 'edcbabcde']
'''

#23 product()

from itertools import *
import pprint

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()

'''RESULTS:
 2H  2D  2C  2S 
 3H  3D  3C  3S 
 4H  4D  4C  4S 
 5H  5D  5C  5S 
 6H  6D  6C  6S 
 7H  7D  7C  7S 
 8H  8D  8C  8S 
 9H  9D  9C  9S 
10H 10D 10C 10S 
 JH  JD  JC  JS 
 QH  QD  QC  QS 
 KH  KD  KC  KS 
 AH  AD  AC  AS 
'''
# or change arguments for another chain

from itertools import *
import pprint

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

DECK = list(
    product(
        SUITS,
        chain(range(2, 11), FACE_CARDS),
    )
)

for card in DECK:
    print('{:>2}{}'.format(card[1], card[0]), end=' ')
    if card[1] == FACE_CARDS[-1]:
        print()

'''RESULTS:
2H  3H  4H  5H  6H  7H  8H  9H 10H  JH  QH  KH  AH 
 2D  3D  4D  5D  6D  7D  8D  9D 10D  JD  QD  KD  AD 
 2C  3C  4C  5C  6C  7C  8C  9C 10C  JC  QC  KC  AC 
 2S  3S  4S  5S  6S  7S  8S  9S 10S  JS  QS  KS  AS 
'''

#24 product() repeat

from itertools import *

def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()

print('Repeat 2:\n')
show(list(product(range(3), repeat=2)))
print('Repeat 3:\n')
show(list(product(range(3), repeat=3)))

'''REPEAT:
Repeat 2:

(0, 0) (0, 1) (0, 2) 
(1, 0) (1, 1) (1, 2) 
(2, 0) (2, 1) (2, 2) 

Repeat 3:

(0, 0, 0) (0, 0, 1) (0, 0, 2) 
(0, 1, 0) (0, 1, 1) (0, 1, 2) 
(0, 2, 0) (0, 2, 1) (0, 2, 2) 
(1, 0, 0) (1, 0, 1) (1, 0, 2) 
(1, 1, 0) (1, 1, 1) (1, 1, 2) 
(1, 2, 0) (1, 2, 1) (1, 2, 2) 
(2, 0, 0) (2, 0, 1) (2, 0, 2) 
(2, 1, 0) (2, 1, 1) (2, 1, 2) 
(2, 2, 0) (2, 2, 1) (2, 2, 2) 
'''

#25 permutations()

from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

print('All permutation:\n')
show(permutations('abcd'))

print('\nPairs:\n')
show(permutations('abcd', r=2))

'''RESULTS:
All permutation:

abcd abdc acbd acdb adbc adcb 
bacd badc bcad bcda bdac bdca 
cabd cadb cbad cbda cdab cdba 
dabc dacb dbac dbca dcab dcba 

Pairs:

ab ac ad 
ba bc bd 
ca cb cd 
da db dc 
'''

#26 combinations()

from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

print('Unique pairs:\n')
show(combinations('abcd', r=2))

'''RESULTS:
Unique pairs:

ab ac ad 
bc bd 
cd 
'''

#27 combinataion_with_replacement()

from itertools import *

def show1(iterable):
    first1 = None
    for i, item in enumerate(iterable, 1):
        if first1 != item[0]:
            if first1 is not None:
                print()
            first1 = item[0]
        print(''.join(item), end=' ')
    print()
print('Unique pairs:\n')
show1(combinations_with_replacement('abcd', r=2))

'''RESULTS:
aa ab ac ad 
bb bc bd 
cc cd 
dd 
'''
