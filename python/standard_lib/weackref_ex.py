"""Weak refferals about."""

import weakref

class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))

obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
print()
'''RESULTS:
obj: <__main__.ExpensiveObject object at 0x7f49e7c9ffd0>
ref: <weakref at 0x7f49e7c4e8e0; to 'ExpensiveObject' at 0x7f49e7c9ffd0>
r(): <__main__.ExpensiveObject object at 0x7f49e7c9ffd0>
deleting obj
(Deleting <__main__.ExpensiveObject object at 0x7f49e7c9ffd0>)
r(): None
'''

#2 weakref callback

import weakref

class ExpensiveObject01:
    
    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    """Call when targeted obj is deleted."""
    print('callback({!r})'.format(reference))

obj01 = ExpensiveObject01()
r = weakref.ref(obj01, callback)

print('obj:', obj01)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj01
print('r():', r())
print()
'''RESULTS:
obj: <__main__.ExpensiveObject01 object at 0x7fa30196bee0>
ref: <weakref at 0x7fa301963f60; to 'ExpensiveObject01' at 0x7fa30196bee0>
r(): <__main__.ExpensiveObject01 object at 0x7fa30196bee0>
deleting obj
(Deleting <__main__.ExpensiveObject01 object at 0x7fa30196bee0>)
callback(<weakref at 0x7fa301963f60; dead>)
r(): None
'''

#3 weakref with finalize()

import weakref

class ExpensiveObject02:
    
    def __del__(self):
        print('Deleting {})'.format(self))

def on_finalize(*args):
    print('on_finalize({!r})'.format(args))

obj02 = ExpensiveObject02()
weakref.finalize(obj02, on_finalize, 'extra argument')

del obj02

'''RESULTS:
Deleting <__main__.ExpensiveObject02 object at 0x7f85e0387ee0>)
on_finalize(('extra argument',))
'''

#4 weakref valuedict for garbage collector

import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('    (Deleting {})'.format(self))

def demo(cache_factory):
    # keep objects
    all_refs = {}
    # make a cach
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # down one ref counter

    print('  all_refs =', end='  ')
    pprint(all_refs)
    print('\n Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
        del value  # down one ref counter

    # dell all refs not include cache
    print('\n Cleanup:')
    del all_refs
    gc.collect()

    print('\n After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
    print('  demo returning')
    return

demo(dict)
print()

demo(weakref.WeakValueDictionary)

'''RESULTS:
CACHE TYPE: <class 'dict'>
  all_refs =  {'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}

 Before, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)

 Cleanup:

 After, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)
  demo returning
    (Deleting ExpensiveObject(one))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(three))

CACHE TYPE: <class 'weakref.WeakValueDictionary'>
  all_refs =  {'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}

 Before, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)

 Cleanup:
    (Deleting ExpensiveObject(one))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(three))

 After, cache contains: []
  demo returning
'''
