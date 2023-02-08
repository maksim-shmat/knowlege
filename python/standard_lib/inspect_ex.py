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

import inspect
import example

'''
sig = inspect.signature(example.module_level_function)
print('module_level_function{}'.format(sig))

print('\nParameter details:')
for name, param in sig.parameters.items():
    if param.kind == inspect.Parameter.POSITIONAL_ONLY:
        print('  {} (positionsl-only)'.format(name))
    elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
        if param.default != inspect.Parameter.empty:
            print(' {}={!r}'.format(name, param.default))
        else:
            print(' {}'.format(name))
    elif param.kind == inspect.Parameter.KEYWORD_ONLY:
        if param.default != inspect.Parameter.empty:
            print('  {}={!r} (keyword-only)'.format(
                name, param.default))
        else:
            print('  {} (keyword-only)'.format(name))
    elif param.kind == inspect.Parameter.VAR_KEYWORD:
        print(' **{}'.format(name))

RESULTS:
module_level_function(arg1, arg2='default', *args, **kwargs)

Parameter details:
 arg1
 arg2='default'
 **kwargs
'''

#12 inspect signature bind

import inspect
import example

'''
sig = inspect.signature(example.module_level_function)

bound = sig.bind(
        'this is arg1',
        'this is arg2',
        'this is an extra positional argument',
        extra_named_arg='value',
)

print('Arguments:')
for name, value in bound.arguments.items():
    print('{} = {!r}'.format(name, value))

print('\nCalling:')
print(example.module_level_function(*bound.args, **bound.kwargs))

RESULTS:
Arguments:
arg1 = 'this is arg1'
arg2 = 'this is arg2'
args = ('this is an extra positional argument',)
kwargs = {'extra_named_arg': 'value'}

Calling:
this is arg1this is arg1
'''

#13 inspect signature bind partial

import inspect
import example

'''
sig = inspect.signature(example.module_level_function)

partial = sig.bind_partial(
        'this is arg1',
)

print('Without defaults:')
for name, value in partial.arguments.items():
    print('{} = {!r}'.format(name, value))

print('\nWith defaults:')
partial.apply_defaults()
for name, value in partial.arguments.items():
    print('{} = {!r}'.format(name, value))

RESULTS:
Without defaults:
arg1 = 'this is arg1'

With defaults:
arg1 = 'this is arg1'
arg2 = 'default'
args = ()
kwargs = {}
'''

#14 inspect getclasstree

import inspect
import example

'''
class C(example.B):
    pass


class D(C, example.A):
    pass


def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent + 1)
    else:
        print(' ' * indent, tree[0].__name__)
    return

if __name__ == '__main__':
    print('A, B, C, D:')
    print_class_tree(inspect.getclasstree(
        [example.A, example.B, C, D])
    )

RESULTS:
A, B, C, D:
 object
  A
   D
   B
    C
     D
'''

#15 inspect getclasstree unique

import inspect
import example

'''
class C(example.B):
    pass


class D(C, example.A):
    pass


def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent + 1)
    else:
        print('  ' * indent, tree[0].__name__)
    return

if __name__ == '__main__':
    print('A, B, C, D:')
    print_class_tree(inspect.getclasstree(
        [example.A, example.B, C, D],
        unique = True,
))

RESULTS:
A, B, C, D:
 object
   A
     B
       C
         D
'''

#16 inspect getmro

import inspect
import example

'''
class C(object):
    pass


class C_First(C, example.B):
    pass


class B_First(example.B, C):
    pass


print('B_First:')
for c in inspect.getmro(B_First):
    print(' {}'.format(c.__name__))
print()
print('C_First:')
for c in inspect.getmro(C_First):
    print('  {}'.format(c.__name__))

RESULTS:
B_First:
 B_First
 B
 A
 C
 object

C_First:
  C_First
  C
  B
  A
  object
'''

#17 inspect currentframe

import inspect
import pprint

'''
def recurse(limit, keyword='default', *, kwonly='must be named'):
    local_variable = '.' * limit
    keyword = 'changed value of argument'
    frame = inspect.currentframe()
    print('line {} of {}'.format(frame.f_lineno,
                                 frame.f_code.co_filename))
    print('locals:')
    pprint.pprint(frame.f_locals)
    print()
    if limit <= 0:
        return
    recurse(limit - 1)
    return local_variable

if __name__ == '__main__':
    recurse(2)

RESULTS:
line 398 of <stdin>
locals:
{'frame': <frame at 0x7f5146f41090, file '<stdin>', line 401, code recurse>,
 'keyword': 'changed value of argument',
 'kwonly': 'must be named',
 'limit': 2,
 'local_variable': '..'}

line 398 of <stdin>
locals:
{'frame': <frame at 0x563bd0f233a0, file '<stdin>', line 401, code recurse>,
 'keyword': 'changed value of argument',
 'kwonly': 'must be named',
 'limit': 1,
 'local_variable': '.'}

line 398 of <stdin>
locals:
{'frame': <frame at 0x563bd0f40fe0, file '<stdin>', line 401, code recurse>,
 'keyword': 'changed value of argument',
 'kwonly': 'must be named',
 'limit': 0,
 'local_variable': ''}
'''

#18 inspect stack

import inspect
import pprint


def show_stack():
    for level in inspect.stack():
        print('{}[{}]\n -> {}'.format(
            level.frame.f_code.co_filename,
            level.lineno,
            level.code_context[level.index].strip(),
        ))
        pprint.pprint(level.frame.f_locals)
        pritn()

def recurse(limit):
    local_variable = '.' * limit
    if limit <= 0:
        show_stack()
        return
    recurse(limit - 1)
    return local_variable

if __name__ == '__main__':
    recurse(2)
