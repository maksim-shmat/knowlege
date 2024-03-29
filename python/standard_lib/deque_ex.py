"""deque() from collections of standard lib about."""

#1 Mother of stacks

import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

'''RESULTS:
Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
Length: 7
Left end: a
Right end: g
remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])
'''

#2 Add elements to both ends

import collections

# add to right end
d1 = collections.deque()
d1.extend('abcdefg')
print('extend:', d1)
d1.append('h')
print('append:', d1)

# add to left end
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

'''RESULTS:
extend: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft: deque([5, 4, 3, 2, 1, 0])
appendleft: deque([6, 5, 4, 3, 2, 1, 0])
'''

#3 pop() and popleft() from both ends

import collections

print('From the right:')
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print()
print('\nFrom the left:')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
print()

'''RESULTS:
From the right:
gfedcba

From the left:
012345
'''
#4 Both ends with separate threads

import collections
import threading
import time

candle = collections.deque(range(5))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return

left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

'''RESULTS:
 Left: 0
Right: 4
 Left: 1
Right: 3
 Left: 2
Right done
 Left done
'''
#5 deque rotate

import collections

d = collections.deque(range(10))
print('Normal:', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right ratation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation:', d)

'''RESULTS:
Normal: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Right ratation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
Left rotation: deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
'''

#6 deque max length

import collections
import random

random.seed(1)  # start random from 1

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)

'''RESULTS:
n = 17
D1: deque([17], maxlen=3)
D2: deque([17], maxlen=3)
n = 72
D1: deque([17, 72], maxlen=3)
D2: deque([72, 17], maxlen=3)
n = 97
D1: deque([17, 72, 97], maxlen=3)
D2: deque([97, 72, 17], maxlen=3)
n = 8
D1: deque([72, 97, 8], maxlen=3)
D2: deque([8, 97, 72], maxlen=3)
n = 32
D1: deque([97, 8, 32], maxlen=3)
D2: deque([32, 8, 97], maxlen=3)
'''
