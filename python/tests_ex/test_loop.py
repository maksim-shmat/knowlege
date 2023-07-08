"""Performances."""

#1

from time import time


mx = 5000

t = time()  # start time for the for loop
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print('for loop: {:.4f} s'.format(time() - t))  # elapsed time

t = time()  # start time ro the list comprehension
compr = [
        divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f} s'.format(time() - t))

t = time()  # start time for the generator expression
gener = list(
        divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t))

# RESULTS:
'''
for loop: 1.8664 s
list comprehension: 1.2511 s
generator expression: 1.3096 s
'''

#2 performance map

from time import time

mx = 2 * 10 ** 7  # 20_000_000

t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print('for loop: {:.4f} s'.format(time() - t))

t = time()
abslist = [abs(n) for n in range(mx)]
print('list comprehension: {:.4f} s'.format(time() - t))

t = time()
absmap = list(map(abs, range(mx)))
print('map: {:.4f} s'.format(time() - t))

# RESULTS:

for loop: 1.8740 s
list comprehension: 1.2294 s
generator expression: 1.2828 s
==============================
for loop: 1.8447 s
list comprehension: 0.9395 s
map: 0.5861 s  # !!
