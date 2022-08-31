"""defaultdict() from collections in standard lib about."""

#1

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

'''RESULTS:
d: defaultdict(<function default_factory at 0x7f192e6dbd90>, {'foo': 'bar'})
foo => bar
bar => default value
'''
