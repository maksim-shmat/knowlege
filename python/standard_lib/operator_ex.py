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

#4 sequences

from operator import *

a = [1, 2, 3]
b = ['a', 'b', 'c']

print('a =', a)
print('b =', b)

print('\Constructive:')
print('  concat(a, b):', concat(a, b))

print('\nSearching:')
print('  contains(a, 1)  :', contains(a, 1))
print('  contains(b, "d"):', contains(b, "d"))
print('  countOf(a, 1)   :', countOf(a, 1))
print('  countOf(b, "d") :', countOf(b, "d"))
print('  indexOf(a, 5)   :', indexOf(a, 1))

print('\nAccess Items:')
print('getitem(b, 1):', getitem(b, 1))
print('getitem(b, slice(1, 3)):', getitem(b, slice(1, 3)))
print('setitem(b, 1, "d"):', end=' '), setitem(b, 1, "d")
print(b)
print('setitem(a, slice(1, 3), [4, 5]:', end=' '), setitem(a, slice(1, 3), [4, 5])
print(a)

print('\nDestructive:')
print('delitem(b, 1):', end=' '), delitem(b, 1)
print(b)
print('delitem(a, slice(1, 3)):', end=' '), delitem(a, slice(1, 3))
print(a)

'''RESULTS:
a = [1, 2, 3]
b = ['a', 'b', 'c']
\Constructive:
  concat(a, b): [1, 2, 3, 'a', 'b', 'c']

Searching:
  contains(a, 1)  : True
  contains(b, "d"): False
  countOf(a, 1)   : 1
  countOf(b, "d") : 0
  indexOf(a, 5)   : 0

Access Items:
getitem(b, 1): b
getitem(b, slice(1, 3)): ['b', 'c']
setitem(b, 1, "d"): ['a', 'd', 'c']
setitem(a, slice(1, 3), [4, 5]: [1, 4, 5]

Destructive:
delitem(b, 1): ['a', 'c']
delitem(a, slice(1, 3)): [1]
'''

#5 inplace

from operator import *

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print()

a = iadd(a, b)
print('a = iadd(a, b) =>', a)
print()

c = iconcat(c, d)
print('c = iconcat(c, d) =>', c)

'''RESULTS:
a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']

a = iadd(a, b) => 4.0

c = iconcat(c, d) => [1, 2, 3, 'a', 'b', 'c']
'''

#6 attrgetter

from operator import *

class MyObj:
    """Class example for attrgetter."""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

l = [MyObj(i) for i in range(5)]
print('objects:', l)

# Get value 'arg' from every object
g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values:', vals)

# Sort with arg
l.reverse()
print('reversed:', l)
print('sorted:', sorted(l, key=g))

'''RESULTS:
objects: [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
arg values: [0, 1, 2, 3, 4]
reversed: [MyObj(4), MyObj(3), MyObj(2), MyObj(1), MyObj(0)]
sorted: [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
'''

#7 itemgetter

from operator import *

l = [dict(val=-1 * i) for i in range(4)]
print('Dictionaries:')
print(' original:', l)
g = itemgetter('val')
vals = [g(i) for i in l]
print(' values:', vals)
print(' sorted:', sorted(l, key=g))

print()
l = [(i, i * -2) for i in range(4)]
print('\nTuples:')
print(' original:', l)
g = itemgetter(1)
vals = [g(i) for i in l]
print('    values:', vals)
print('    sorted:', sorted(l, key=g))

'''RESULTS:
Dictionaries:
 original: [{'val': 0}, {'val': -1}, {'val': -2}, {'val': -3}]
 values: [0, -1, -2, -3]
 sorted: [{'val': -3}, {'val': -2}, {'val': -1}, {'val': 0}]


Tuples:
 original: [(0, 0), (1, -2), (2, -4), (3, -6)]
    values: [0, -2, -4, -6]
    sorted: [(3, -6), (2, -4), (1, -2), (0, 0)]
'''

#8 operator classes

from operator import *

class MyObj:
    """E.g."""

    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return 'MyObj({})'.format(self.val)

    def __lt__(self, other):
        """Less than."""
        print('Testing {} < {}'.format(self, other))
        return self.val < other.val

    def __add__(self, other):
        """Sum of values."""
        print('Adding {} + {}'.format(self, other))
        return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)

print('Comparison:')
print(lt(a, b))
print('\nArithmetic:')
print(add(a, b))

'''RESULTS:
Comparison:
Testing MyObj(1) < MyObj(2)
True

Arithmetic:
Adding MyObj(1) + MyObj(2)
MyObj(3)
'''
