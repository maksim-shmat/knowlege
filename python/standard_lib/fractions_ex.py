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
