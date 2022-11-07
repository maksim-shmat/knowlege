"""Pickle serialization about."""

######1 Python picling or serializing

import pickle

marks = {'Alex': 87, 'Lenin': 98, 'Kuwabara': 90}
picklefile1 = open('marks', 'wb')
pickle.dump(marks, picklefile1)
picklefile1.close()

######2 Python unpacking or deserializing

import pickle

picklefile2 = open('marks', 'rb')
marks = pickle.load(picklefile2)
picklefile2.close()
print(marks)
print(type(marks))

######3 Pickle a custom python class object

import pickle

class Laptop:

    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

    def details(self):
        print('The details of the laptop are:')
        print('Name        :', self.name)
        print('Processor   :', self.processor)
        print('HDD Capacity:', self.hdd)
        print('RAM         :', self.ram)
        print('Cost($)     :', self.cost)

# create objedt
laptop1 = Laptop('Dell Alienware', 'Intel Core i7', 512, 8, 2500.00)

# create a pickle file
picklefile3 = open('laptop1', 'wb')
# pickle the dictionary and write it to file
pickle.dump(laptop1, picklefile3)
picklefile3.close()

### unpickle python custom class object

import pickle

class Laptop:
    
    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

    def details(self):
        print('The details of the laptop are: ')
        print('Name         : ', self.name)
        print('Processorus  : ', self.processor)
        print('HDD Capacity : ', self.hdd)
        print('RAM          : ', self.ram)
        print('Cost($)      : ', self.cost)

# read the pickle file
picklefile4 = open('laptop1', 'rb')
# unpickle the dataframe
laptop1 = pickle.load(picklefile4)
#close file
picklefile4.close()

print(type(laptop1))
laptop1.details()

######4 Pickle a dataframe

import numpy as np
import pandas as pd
import pickle

# dataframe
df = pd.DataFrame(
        [['Suomi', 68, 84, 78, 96],
         ['Kiki', 74, 56, 77, 98],
         ['Anlal', 77, 68, 52, 89],
         ['Lenin', 89, 23, 34, 86]],
         columns=['name', 'phisics', 'chemistry', 'algebra', 'calculus'])

# create a file
picklefile5 = open('df_marks', 'wb')
# pickle the dataframe
pickle.dump(df, picklefile5)
picklefile5.close()

### Unpickle a dataframe

import numpy as np
import pandas as pd
import pickle

# read the pickle file
picklefile = open('df_marks', 'rb')
# unpickle the dataframe
df = pickle.load(picklefile)
# close file
picklefile.close()

# print the dataframe
print(type(df))
print(df)

#5 new Apr 16

import pickle

shoplistfile = 'jill.data'
shoplist = ['apples', 'mango', 'peackocks']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)  # put object into file
f.close()

del shoplist  # del variable

# unpickling

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)  # load object from file
print(storedlist)

#6 5 Nov. pickle string

import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('DATA:', end=' ')
pprint.pprint(data)

data_string = pickle.dumps(data)
print('PICKLE: {!r}'.format(data_string))

'''RESULTS:
DATA: [{'a': 'A', 'b': 2, 'c': 3.0}]
PICKLE: b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00]\x94}\x94(\x8c\x01a\x94\x8c\x01A\x94\x8c\x01b\x94K\x02\x8c\x01c\x94G@\x08\x00\x00\x00\x00\x00\x00ua.'
'''

#7 unpickle

import pickle
import pprint

print()
data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('BEFORE:', end=' ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print('AFTER:', end=' ')
pprint.pprint(data2)

print('SAME?:', (data1 is data2))
print('EQUAL?:', (data1 == data2))

'''RESULTS:
BEFORE: [{'a': 'A', 'b': 2, 'c': 3.0}]
AFTER: [{'a': 'A', 'b': 2, 'c': 3.0}]
SAME?: False
EQUAL?: True
'''

#8 stream

import io
import pickle
import pprint


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# Imitate file
out_s = io.BytesIO()

# Write in stream
for o in data:
    print('WRITING: {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Set readable stream
in_s = io.BytesIO(out_s.getvalue())

# Read data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ   : {} ({})'.format(o.name, o.name_backwards))

'''RESULTS:
WRITING: pickle (elkcip)
WRITING: preserve (evreserp)
WRITING: last (tsal)
READ   : pickle (elkcip)
READ   : preserve (evreserp)
READ   : last (tsal)
'''

#9 load from file test.dat
'''
import pickle
import pprint
import sys

from pickle_dump_to_file1 import SimpleObject

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print('READ: {} ({})'.format(o.name, o.name_backwards))

   RESULTS:
from CLI: python3 pickle_load_from_file1.py test.dat

READ: pickle (elkcip)
READ: preserve (evreserp)
READ: last (tsal)
'''

#10 __getstate__() and __setstate__()

import pickle


class State:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'State({!r})'.format(self.__dict__)


class MyClass:

    def __init__(self, name):
        print('MyClass.__init__({})'.format(name))
        self._set_name(name)

    def _set_name(self, name):
        self.name = name
        self.computed = name[::-1]

    def __repr__(self):
        return 'MyClass({!r}) (computed={!r})'.format(
                self.name, self.computed)

    def __getstate__(self):
        state = State(self.name)
        print('__getstate__ -> {!r}'.format(state))
        return state

    def __setstate__(self, state):
        print('__setstate__({!r})'.format(state))
        self._set_name(state.name)

inst = MyClass('name here')
print('Before:', inst)

dumped = pickle.dumps(inst)

reloaded = pickle.loads(dumped)
print('After:', reloaded)

'''RESULTS:
MyClass.__init__(name here)
Before: MyClass('name here') (computed='ereh eman')
__getstate__ -> State({'name': 'name here'})
__setstate__(State({'name': 'name here'}))
After: MyClass('name here') (computed='ereh eman')
'''

#10 cycle

import pickle


class Node:
    """Simple digraph."""
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        """Make edge between . and another node."""
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)

def preorder_traversal(root, seen=None, parent=None):
    """Generator-function how return edges for graph."""
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)

def show_edges(root):
    """Show all edges from graph."""
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(
            parent.name, child.name, id(child)))

# Define edges
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

# Add edges between it
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print('ORIGINAL GRAPH:')
show_edges(root)

# Serialisation and deserialisation graph for make new set of nodes
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\nRELOADED GRAPH:')
show_edges(reloaded)

'''RESULTS:
ORIGINAL GRAPH:
 root ->  a (139947175062272)
    a ->  b (139947175061744)
    b ->  a (139947175062272)
    b ->  c (139947175062416)
    a ->  a (139947175062272)
 root ->  b (139947175061744)

RELOADED GRAPH:
 root ->  a (139947175062608)  # not the same nodes-objects but binds the same
    a ->  b (139947175062032)
    b ->  a (139947175062608)
    b ->  c (139947175061936)
    a ->  a (139947175062608)
 root ->  b (139947175062032)
'''
