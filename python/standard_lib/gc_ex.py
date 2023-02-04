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

#3 
