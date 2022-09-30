"""Fractions about."""

#1 create integers

import fractions

for n, d in [(1, 2), (2, 4), (3, 6)]:
    f = fractions.Fraction(n, d)
    print('{}/{} = {}'.format(n, d, f))

'''RESULTS:
1/2 = 1/2
2/4 = 1/2
3/6 = 1/2
'''

#2 create strings

import fractions

print()
for s in ['1/2', '2/4', '3/6']:
    f = fractions.Fraction(s)
    print('{} = {}'.format(s, f))

'''RESULTS:
1/2 = 1/2
2/4 = 1/2
3/6 = 1/2
'''

#3 create strings floatas

import fractions

print()
for s in ['0.5', '1.5', '2.0', '5e-1']:
    f = fractions.Fraction(s)
    print('{0:>4} = {1}'.format(s, f))

'''RESULTS:
0.5 = 1/2
 1.5 = 3/2
 2.0 = 2
5e-1 = 1/2
'''

#4 fractions from float

import fractions

print()
for v in [0.1, 0.5, 1.5, 2.0]:
    print('{} = {}'.format(v, fractions.Fraction(v)))

'''RESULTS:
0.1 = 3602879701896397/36028797018963968
0.5 = 1/2
1.5 = 3/2
2.0 = 2
'''

#5 fractions from decimal

import decimal
import fractions

print()
values = [
        decimal.Decimal('0.1'),
        decimal.Decimal('0.5'),
        decimal.Decimal('1.5'),
        decimal.Decimal('2.0'),
]

for v in values:
    print('{} = {}'.format(v, fractions.Fraction(v)))
print()

'''RESULTS:
0.1 = 1/10
0.5 = 1/2
1.5 = 3/2
2.0 = 2
'''

#6 arithmetic

import fractions

f1 = fractions.Fraction(1, 2)
f2 = fractions.Fraction(3, 4)

print('{} + {} = {}'.format(f1, f2, f1 + f2))
print('{} - {} = {}'.format(f1, f2, f1 - f2))
print('{} * {} = {}'.format(f1, f2, f1 * f2))
print('{} / {} = {}'.format(f1, f2, f1 / f2))
print()

'''RESULTS:
1/2 + 3/4 = 5/4
1/2 - 3/4 = -1/4
1/2 * 3/4 = 3/8
1/2 / 3/4 = 2/3
'''

#7 limit denominator

import fractions
import math

print('PI       =', math.pi)

f_pi = fractions.Fraction(str(math.pi))
print('No limit =', f_pi)

for i in [1, 6, 11, 60, 70, 90, 100]:
    limited = f_pi.limit_denominator(i)
    print('{0:8} = {1}'.format(i, limited))
print()

'''RESULTS:
PI       = 3.141592653589793
No limit = 3141592653589793/1000000000000000
       1 = 3
       6 = 19/6
      11 = 22/7
      60 = 179/57
      70 = 201/64
      90 = 267/85
     100 = 311/99
'''

