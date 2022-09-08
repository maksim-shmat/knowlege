"""functools about."""

#1 reduce() iterate over each item in a list and return a single value

from functools import reduce

def add_num(a, b):
    return a + b
a = [ 1, 2, 3, 10]
print(reduce(add_num, a))
print()

### format a list of strings using the reduce()

from functools import reduce
def add_str(a,b):
    return a+' '+b
a = ['MUO', 'is', 'a', 'media', 'website']
print(reduce(add_str, a))
print()

######2 split()

words = "column1 column2 column3"
words = words.split(" ")
print(words)
print()

######3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
    print(i, j)
print()

###3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
    print(i, j)
print()

###3 enumerate()

fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):   # ...enumerate(fruits, start=1): - not from 0
    print(i, j)
print()

### standard?

fruits = ["grape", "apple", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])
print()

#1 functools partial

import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print('  called myfunc with:', (a, b))

def show_details(name, f, is_partial=False):
    """Show details called object."""
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return

show_details('myfunc', myfunc)
myfunc('a', 3)
print()

# if is default value for 'b', but return 'a'

p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)
p1('passing a')
p1('override b', b=5)
print()

# Make default value for 'a' and 'b'
p2 =functools.partial(myfunc, a=8, b=88)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')
print()
'''RESULTS:
myfunc:
  object: <function myfunc at 0x7f39132252d0>
  __name__: myfunc
  called myfunc with: ('a', 3)

partial with named default:
  object: functools.partial(<function myfunc at 0x7f39132252d0>, b=4)
  func: <function myfunc at 0x7f39132252d0>
  args: ()
  keywords: {'b': 4}
  called myfunc with: ('passing a', 4)
  called myfunc with: ('override b', 5)

partial with defaults:
  object: functools.partial(<function myfunc at 0x7f48ad13d2d0>, a=8, b=88)
  func: <function myfunc at 0x7f48ad13d2d0>
  args: ()
  keywords: {'a': 8, 'b': 88}
  called myfunc with: (8, 88)
  called myfunc with: (8, 'override b')
'''

#2 functools update_wrapper() copy attributes __doc__ and __name__ 
# from core func for partial obj

import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print('  called myfunc with:', (a, b))

def show_details(name, f):
    """Show details called object."""
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    print()

show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper:')
print('  assign:', functools.WRAPPER_ASSIGNMENTS)
print('  update:', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)

'''RESULTS:
myfunc:
  object: <function myfunc at 0x7fb61441d360>
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

raw wrapper:
  object: functools.partial(<function myfunc at 0x7fb61441d360>, b=4)
  __name__: (no __name__)
  __doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'

Updating wrapper:
  assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
  update: ('__dict__',)

updated wrapper:
  object: functools.partial(<function myfunc at 0x7fb61441d360>, b=4)
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

'''

#3 functools any callable object

import functools

class MyClass:
    """Demonstrational class for functools."""

    def __call__(self, e, f=6):
        """Docstring for MyClass.__call__"""
        print('  called objct with:', (self, e, f))

    def show_details(name, f):
        """Show details of called object."""
        print('{}:'.format(name))
        print('  object:', f)
        print('  __name__:', end=' ')
        try:
            print(f.__name__)
        except AttributeError:
            print('no __name__)')
        print('  __doc__', repr(f.__doc__))
        return

o = MyClass()

show_details('instance', o)
o('e goes here')
print()

p = functools.partial(o, e='default for e', f=8)
functools.update_wrapper(p, o)
show_details('instance wrapper', p)
p()

'''RESULTS:
instance:
  object: <__main__.MyClass object at 0x7fc75b7efbe0>
  __name__: (no __name__)
  __doc__ 'Demonstrational class for functools.'

  called objct with: (<__main__.MyClass object at 0x7fc75b7efbe0>, 'e goes here', 6)

instance wrapper:
  object: functools.partial(<__main__.MyClass object at 0x7fc75b7efbe0>, e='default for e', f=8)
  __name__: (no __name__)
  __doc__ 'Demonstrational class for functools.'

  called objct with: (<__main__.MyClass object at 0x7fc75b7efbe0>, 'default for e', 8)
'''
#4 functools total ordering

import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('  testing __eq__({}, {})'.format(
            self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('  testing __gt__({}, {})'.format(
            self.val, other.val))
        return self.val > other.val

print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print('\nComparisons:')
for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
    print('\n{:<6}:'.format(expr))
    result = eval(expr)
    print('  result of {}: {}'.format(expr, result))

'''RESULTS:
Methods:

[('__eq__', <function MyObject.__eq__ at 0x7f566712ecb0>),
 ('__ge__', <function _ge_from_gt at 0x7f566740dea0>),
 ('__gt__', <function MyObject.__gt__ at 0x7f566712ed40>),
 ('__init__', <function MyObject.__init__ at 0x7f56672f3400>),
 ('__le__', <function _le_from_gt at 0x7f566740df30>),
 ('__lt__', <function _lt_from_gt at 0x7f566740de10>)]

Comparisons:

a < b :
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a < b: True

a <= b:
  testing __gt__(1, 2)
  result of a <= b: True

a == b:
  testing __eq__(1, 2)
  result of a == b: False

a >= b:
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a >= b: False

a > b :
  testing __gt__(1, 2)
  result of a > b: False
'''

#5 lru_cache

import functools

@functools.lru_cache()
def expensive(a, b):
    print('expensive({}, {})'.format(a, b))
    return a * b

MAX = 2

print("First set of calls:")
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThisrd set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)

print(expensive.cache_info())

'''RESULTS:
First set of calls:
expensive(0, 0)
expensive(0, 1)
expensive(1, 0)
expensive(1, 1)
CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)

Second set of calls:
expensive(0, 2)
expensive(1, 2)
expensive(2, 0)
expensive(2, 1)
expensive(2, 2)
CacheInfo(hits=4, misses=9, maxsize=128, currsize=9)

Clearing cache:
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

Thisrd set of calls:
expensive(0, 0)
expensive(0, 1)
expensive(1, 0)
expensive(1, 1)
CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)
'''

#6 functools reduce

import functools

def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b

data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data)
print('results: {}'.format(result))

'''RESULTS:
range(1, 5)
do_reduce(1, 2)
do_reduce(3, 3)
do_reduce(6, 4)
results: 10
'''

#7 reduce initializer

