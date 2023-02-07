"""inspect about."""


#1 inspect getmembers module

import inspect
'''
import example


for name, data in inspect.getmembers(example):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))

RESULTS:
A : <class 'example.A'>
B : <class 'example.B'>
instance_of_a : <example.A object at 0x7fc3d841e740>
module_level_function : <function module_level_function at 0x7fc3d8426dd0>
'''

#2 inspect getmembers module class

import inspect
'''
import example


for name, data in inspect.getmembers(example, inspect.isclass):
    print('{} : {!r}'.format(name, data))

RESULTS:
A : <class 'example.A'>
B : <class 'example.B'>
'''

#3 inspect getmembers class

import inspect
from pprint import pprint
'''
import example


pprint(inspect.getmembers(example.A), width=65)
'''

#4 inspect getmembers class methds

import inspect
from pprint import pprint
'''
import example

pprint(inspect.getmembers(example.A, inspect.isfunction))
print()
pprint(inspect.getmembers(example.B, inspect.isfunction))

RESULTS:
[('__init__', <function A.__init__ at 0x7fd163936950>),
 ('get_naem', <function A.get_naem at 0x7fd1639369e0>)]

[('__init__', <function A.__init__ at 0x7fd163936950>),
 ('do_something', <function B.do_something at 0x7fd163936a70>),
 ('get_naem', <function A.get_naem at 0x7fd1639369e0>),
 ('get_name', <function B.get_name at 0x7fd163936b00>)]
'''

#5 inspect getmembers instance

import inspect
from pprint import pprint
'''
import example

a = example.A(name='inspect_getmembers')
pprint(inspect.getmembers(a, inspect.ismethod))

RESULTS:
[('__init__',
  <bound method A.__init__ of <example.A object at 0x7f4d94f8ffd0>>),
 ('get_naem',
  <bound method A.get_naem of <example.A object at 0x7f4d94f8ffd0>>)]
'''

#6 inspect getdoc

import inspect
'''
import example

print('B.__doc__:')
print(example.B.__doc__)
print()
print('getdoc(B):')
print(inspect.getdoc(example.B))

RESULTS:  # No expected
B.__doc__:
None

getdoc(B):
The A class
'''

#7 inspect getcomments method

import inspect
'''
import example

print(inspect.getcomments(example.B.do_something))

RESULTS:
#This method is not part of A.
'''

#8 inspect getsource class

import inspect
'''
import example

print(inspect.getsource(example.A))

RESULTS:
class A(object):
    """The A class"""

    def __init__(self, name):
        self.name = name

    def get_naem(self):
        "Returns the name of the instance."
        return self.name
'''

#9 inspect get source method

import inspect
'''
import example

print(inspect.getsource(example.A.get_naem))

RESULTS:
    def get_naem(self):
        "Returns the name of the instance."
        return self.name
'''

#10 inspect getsourcelines method

import inspect
import pprint
'''
import example

pprint.pprint(inspect.getsourcelines(example.A.get_naem))

RESULTS:
(['    def get_naem(self):\n',
  '        "Returns the name of the instance."\n',
  '        return self.name\n'],
 24)
'''

#11 inspect signature function
