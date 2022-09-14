"""Operator about."""

#1 check identical.

from operator import *

a = -1
b = 5

print('a =', a)
print('b =', b)
print()

print('not_(a)        :', not_(a))
print('truth(a)       :', truth(a))
print('is_(a, b)      :', is_(a, b))
print('is_not(a, b)   :', is_not(a, b))

'''RESULTS:
a = -1
b = 5

not_(a)        : False
truth(a)       : True
is_(a, b)      : False
is_not(a, b)   : True
'''

#2 collation

a = 1
b = 5.0

print('a =', a)
print('b =', b)
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))

'''RESULTS:
a = 1
b = 5.0
lt(a, b): True   # <
le(a, b): True   # <=
eq(a, b): False  # ==
ne(a, b): True   # !=
ge(a, b): False  # >=
gt(a, b): False  # >
'''

#3 math operators

a = -1
b = 5.0
c = 2
d = 6

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

print('\nPositive/Negative:')
print('abs(a):', abs(a))
print('neg(a):', neg(a))
print('neg(b):', neg(b))
print('pos(a):', pos(a))
print('pos(b):', pos(b))

print('\nArithmetic:')
print('add(a, b) :', add(a, b))
print('floordiv(a, b) :', floordiv(a, b))
print('floordiv(d, c) :', floordiv(d, c))
print('mod(a, b) :',  mod(a, b))
print('mul(a, b) :', mul(a, b))
print('pow(c, d) :', pow(c, d))
print('sub(b, a) :', sub(b, a))
print('truediv(a, b) :', truediv(a, b))
print('truediv(d, c):', truediv(d, c))

print('\nBitwise:')
print('and_(c, d) :', and_(c, d))
print('invert(c) :', invert(c))
print('lshift(c, d):', lshift(c, d))
print('or_(c, d) :', or_(c, d))
print('rshift(d, c) :', rshift(d, c))
print('xor(c, d) :', xor(c, d))

'''RESULTS:
Positive/Negative:
abs(a): 1
neg(a): 1
neg(b): -5.0
pos(a): -1
pos(b): 5.0

Arithmetic:
add(a, b) : 4.0
floordiv(a, b) : -1.0
floordiv(d, c) : 3
mod(a, b) : 4.0
mul(a, b) : -5.0
pow(c, d) : 64
sub(b, a) : 6.0
truediv(a, b) : -0.2
truediv(d, c): 3.0

Bitwise:
and_(c, d) : 2
invert(c) : -3
lshift(c, d): 128
or_(c, d) : 6
rshift(d, c) : 1
xor(c, d) : 4
'''

#4
