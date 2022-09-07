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

#3
