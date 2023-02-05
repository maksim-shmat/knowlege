"""garbage collector about."""

#1 gc get referents

import gc
import pprint

'''
class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
                self.__class__.__name__, self.name)

# Create cyclic grph
one = Graph('one')
two = Graph('two')
three = Graph('three')

one.set_next(two)
two.set_next(three)
three.set_next(one)

print()
print('three refers to:')
for r in gc.get_referents(three):
    pprint.pprint(r)

RESULTS:
Linking nodes Graph(one).next = Graph(two)
Linking nodes Graph(two).next = Graph(three)
Linking nodes Graph(three).next = Graph(one)

three refers to:
{'name': 'three', 'next': Graph(one)}
<class '__main__.Graph'>
'''

#2 gc get referents cycle

import gc
import pprint
import queue

'''
class Graph:
    
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
                self.__class__.__name__, self.name)

# Create a cyclic graph

one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

print()

seen = set()
to_process = queue.Queue()

# Start with empty chain of objects and node named 'three
to_process.put(([], three))

while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print('Examining:', repr(next))
    seen.add(id(next))
    for r in gc.get_referents(next):
        if isinstance(r, str) or isinstance(r, type):
            # Ignore strings and classes
            pass
        elif id(r) in seen:
            print()
            print('Found a cycle to {}:'.format(r))
            for i, link in enumerate(chain):
                print(' {}:'.format(i), end=' ')
                pprint.pprint(link)
        else:
            to_process.put((chain, r))

RESULTS:
Linking nodes Graph(one).next = Graph(two)
Linking nodes Graph(two).next = Graph(three)
Linking nodes Graph(three).next = Graph(one)

Examining: Graph(three)
Examining: {'name': 'three', 'next': Graph(one)}
Examining: Graph(one)
Examining: {'name': 'one', 'next': Graph(two)}
Examining: Graph(two)
Examining: {'name': 'two', 'next': Graph(three)}

Found a cycle to Graph(three):
 0: Graph(three)
 1: {'name': 'three', 'next': Graph(one)}
 2: Graph(one)
 3: {'name': 'one', 'next': Graph(two)}
 4: Graph(two)
 5: {'name': 'two', 'next': Graph(three)}
'''

#3 gc collect

import gc
import pprint

'''i
class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{} ({})'.format(
                self.__class__.__name__, self.name)

one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Remove links on the nodes from namefiled of this module
one = two = three = None

# Demonstrate gc effect
for i in  range(2):
    print('\nCollecting {} ...'.format(i))
    n = gc.collect()
    print('Unreachable objects:', n)
    print('Remaining Garbage:', end=' ')
    pprint.pprint(gc.garbage)

RESULTS:
Linking nodes Graph (one).next = Graph (two)
Linking nodes Graph (two).next = Graph (three)
Linking nodes Graph (three).next = Graph (one)

Collecting 0 ...
Unreachable objects: 34
Remaining Garbage: []

Collecting 1 ...
Unreachable objects: 0
Remaining Garbage: []
'''

#4 gc get referrers

import gc
import pprint

'''
class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
                self.__class__.__name__, self.name)

    def __del__(self):
        print('{}.__del__()'.format(self))

one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Then gc save object as not condition against garbage
print()
print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', end=' ')
pprint.pprint(gc.garbage)

# Ignore links from local variables from this module, global var and from gc journal
REFERRERS_TO_IGNORE = [locals(), globals(), gc.garbage]


def find_referring_graphs(obj):
    print('Looking for references to {!r}'.format(obj))
    referrers = (r for r in gc.get_referrers(obj)
            if r not in REFERRERS_TO_IGNORE)
    for ref in referrers:
        if isinstance(ref, Graph):
            # Node of graph
            yield ref
        elif isinstance(ref, dict):
            # Dict of exsemlar or other name field
            for parent in find_referring_graphs(ref):
                yield parent

# Find object how linked on the graph objects
print()
print('Clearing referrers:')
for obj in [one, two, three]:
    for ref in find_referring_graphs(obj):
        print('Found referrer:', ref)
        ref.set_next(None)
        del ref  # del link for del node
    del obj  # del link for del node

# Del links from gc.garbage
print()
print('Clearing gc.garbage:')
del gc.garbage[:]

# Del all objects
print()
print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', end=' ')
pprint.pprint(gc.garbage)

RESULTS:
Linking nodes Graph(one).next = Graph(two)
Linking nodes Graph(two).next = Graph(three)
Linking nodes Graph(three).next = Graph(one)

Collecting...
Unreachable objects: 28
Remaining Garbage: []

Clearing referrers:
Looking for references to Graph(one)
Looking for references to {'name': 'three', 'next': Graph(one)}
Found referrer: Graph(three)
Linking nodes Graph(three).next = None
Looking for references to Graph(two)
Looking for references to {'name': 'one', 'next': Graph(two)}
Found referrer: Graph(one)
Linking nodes Graph(one).next = None
Looking for references to Graph(three)
Looking for references to {'name': 'two', 'next': Graph(three)}
Found referrer: Graph(two)
Linking nodes Graph(two).next = None

Clearing gc.garbage:

Collecting...
Unreachable objects: 0
Remaining Garbage: []
Graph(one).__del__()
Graph(two).__del__()
Graph(three).__del__()
'''

#5 gc get_threshold()

import gc

'''
print(gc.get_threshold())

RESULTS:
(700, 10, 10)
'''

#6 gc change threshold

# $ python3 -u gc_threshold.py 5
# $ python3 -u gc_threshold.py 2

import gc
import pprint
import sys

'''
try:
    threshold = int(sys.argv[1])
except (IndexError, ValueError, TypeError):
    print('Missing or invalid threshold, using default')
    threshold = 5


class MyObj:

    def __init__(self, name):
        self.name = name
        print('Created', self.name)

gc.set_debug(gc.DEBUG_STATS)
gc.st_threshold(threshold, 1, 1)
print('Thresholds:', gc.get_threshold())

print('Clear the collector by forcing a run')
gc.collect()
print()

print('Creating objects')
objs = []
for i in range(10):
    objs.append(MyObj(i))
print('Exiting')

# Debug off
gc.set_debug(0)
'''

#7 gc debug stats

import gc

'''
gc.set_debug(gc.DEBUG_STATS)

gc.collect()
print('Exiting')

RESULTS:
gc: collecting generation 2...
gc: objects in each generation: 628 3681 5035
gc: objects in permanent generation: 0
gc: done, 28 unreachable, 0 uncollectable, 0.0010s elapsed
Exiting
gc: collecting generation 2...
gc: objects in each generation: 0 0 8867
gc: objects in permanent generation: 0
gc: done, 0 unreachable, 0 uncollectable, 0.0008s elapsed
gc: collecting generation 2...
gc: objects in each generation: 164 0 8795
gc: objects in permanent generation: 0
gc: done, 1818 unreachable, 0 uncollectable, 0.0010s elapsed
gc: collecting generation 2...
gc: objects in each generation: 0 0 6151
gc: objects in permanent generation: 0
gc: done, 1476 unreachable, 0 uncollectable, 0.0008s elapsed
gc: collecting generation 2...
gc: objects in each generation: 0 0 4470
gc: objects in permanent generation: 0
gc: done, 1534 unreachable, 0 uncollectable, 0.0009s elapsed
'''

#8 gc debug saveall

import gc

'''
flags = (gc.DEBUG_COLLECTABLE |
         gc.DEBUG_UNCOLLECTABLE |
         gc.DEBUG_SAVEALL
         )

gc.set_debug(flags)


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return '{} ({})'.format(
                self.__class__.__name__, self.name)


class CleanupGraph(Graph):

    def __del__(self):
        print('{}.__del__()'.format(self))

one = Graph('one')
two = Graph('two')
one.set_next(two)
two.set_next(one)

three = CleanupGraph('three')

four = CleanupGraph('four')
five = CleanupGraph('five')
four.set_next(five)
five.set_next(four)

one = two = three = four = five = None

print('Collecting')
gc.collect()
print('Done')

for o in gc.garbage:
    if isinstance(o, Graph):
        print('Retained: {} 0x{:x}'.format(o, id(o)))

gc.set_debug(0)

RESULTS:
gc: collectable <dict 0x7fe7cdb2bbc0>
gc: collectable <dict 0x7fe7cdb2bd00>
gc: collectable <function 0x7fe7cdaf6dd0>
gc: collectable <function 0x7fe7cdaf6e60>
gc: collectable <function 0x7fe7cdaf6ef0>
gc: collectable <function 0x7fe7cdaf6f80>
gc: collectable <member_descriptor 0x7fe7cdb2bb40>
gc: collectable <member_descriptor 0x7fe7cdb2bb80>
gc: collectable <function 0x7fe7cdaf7010>
gc: collectable <function 0x7fe7cdaf70a0>
gc: collectable <function 0x7fe7cdaf7130>
gc: collectable <function 0x7fe7cdaf71c0>
gc: collectable <member_descriptor 0x7fe7cdb2bc80>
gc: collectable <member_descriptor 0x7fe7cdb2bcc0>
gc: collectable <function 0x7fe7cdaf7250>
gc: collectable <function 0x7fe7cdaf72e0>
gc: collectable <function 0x7fe7cdaf7370>
gc: collectable <function 0x7fe7cdaf7400>
gc: collectable <member_descriptor 0x7fe7cdb2bdc0>
gc: collectable <member_descriptor 0x7fe7cdb2be00>
gc: collectable <member_descriptor 0x7fe7cdb2be40>
gc: collectable <Graph 0x7fe7cd94bfd0>
gc: collectable <Graph 0x7fe7cd94be20>
gc: collectable <dict 0x7fe7cda92200>
gc: collectable <dict 0x7fe7cd85dd40>
gc: collectable <CleanupGraph 0x7fe7cd843f70>
gc: collectable <CleanupGraph 0x7fe7cd843ac0>
gc: collectable <dict 0x7fe7cd85cec0>
gc: collectable <dict 0x7fe7cd85d140>
CleanupGraph (four).__del__()
CleanupGraph (five).__del__()
Done
Retained: Graph (one) 0x7fe7cd94bfd0
Retained: Graph (two) 0x7fe7cd94be20
Retained: CleanupGraph (four) 0x7fe7cd843f70
Retained: CleanupGraph (five) 0x7fe7cd843ac0
'''

#9 gc DEBUG_LEAK

import gc

'''
flags = gc.DEBUG_LEAK

gc.set_debug(flags)


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
                self.__class__.__name__, self.name)


class CleanupGraph(Graph):

    def __del__(self):
        print('{}.__del__()'.format(self))

one = Graph('one')
two = Graph('two')
one.set_next(two)
two.set_next(one)

three = CleanupGraph('three')

four = CleanupGraph('four')
five = CleanupGraph('five')
four.set_next(five)
five.set_next(four)

one = two = three = four = five = None

print('Collecting')
gc.collect()
print('Done')

for o in gc.garbage:
    if isinstance(o, Graph):
        print('Retained: {} 0x{:x}'.format(o, id(o)))

gc.set_debug(0)

RESULTS:
gc: collectable <dict 0x7f0d13d27bc0>
gc: collectable <dict 0x7f0d13d27d00>
gc: collectable <function 0x7f0d13cf2dd0>
gc: collectable <function 0x7f0d13cf2e60>
gc: collectable <function 0x7f0d13cf2ef0>
gc: collectable <function 0x7f0d13cf2f80>
gc: collectable <member_descriptor 0x7f0d13d27b40>
gc: collectable <member_descriptor 0x7f0d13d27b80>
gc: collectable <function 0x7f0d13cf3010>
gc: collectable <function 0x7f0d13cf30a0>
gc: collectable <function 0x7f0d13cf3130>
gc: collectable <function 0x7f0d13cf31c0>
gc: collectable <member_descriptor 0x7f0d13d27c80>
gc: collectable <member_descriptor 0x7f0d13d27cc0>
gc: collectable <function 0x7f0d13cf3250>
gc: collectable <function 0x7f0d13cf32e0>
gc: collectable <function 0x7f0d13cf3370>
gc: collectable <function 0x7f0d13cf3400>
gc: collectable <member_descriptor 0x7f0d13d27dc0>
gc: collectable <member_descriptor 0x7f0d13d27e00>
gc: collectable <member_descriptor 0x7f0d13d27e40>
gc: collectable <Graph 0x7f0d13b47fd0>
gc: collectable <Graph 0x7f0d13b47e20>
gc: collectable <dict 0x7f0d13c8e200>
gc: collectable <dict 0x7f0d13a59c80>
gc: collectable <CleanupGraph 0x7f0d13a3ff40>
gc: collectable <CleanupGraph 0x7f0d13a3fa90>
gc: collectable <dict 0x7f0d13a58e40>
gc: collectable <dict 0x7f0d13a59080>
CleanupGraph(four).__del__()
CleanupGraph(five).__del__()
Done
Retained: Graph(one) 0x7f0d13b47fd0
Retained: Graph(two) 0x7f0d13b47e20
Retained: CleanupGraph(four) 0x7f0d13a3ff40
Retained: CleanupGraph(five) 0x7f0d13a3fa90
'''
