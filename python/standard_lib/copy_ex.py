"""copy() and deepcopy() about."""

import copy
import functools

@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)

print('            my_list:', my_list)
print('                dup:', dup)
print('     dup is my_list:', (dup is my_list))
print('     dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

'''RESULTS:
            my_list: [<__main__.MyClass object at 0x7f5bac0cbfd0>]
                dup: [<__main__.MyClass object at 0x7f5bac0cbfd0>]
     dup is my_list: False
     dup == my_list: True
dup[0] is my_list[0]: True
dup[0] == my_list[0]: True
'''

#2 but against with deepcopy()
# ...
# dup = copy.deepcopy(my_list)

'''RESULTS:
             my_list: [<__main__.MyClass object at 0x1018a87b8>]
                 dup: [<__main__.MyClass object at 0x1018b1b70>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: False
dup[0] == my_list[0]: True
'''

#3 deepcopy() against recursion with dict memo

import copy

class Graph:
    
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id{})'.format(
                self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to (!r)'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print('  Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup

root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)

'''RESULTS:
Calling __deepcopy__ for Graph(name=root, id140690800410000)
  Memo dictionary:
    (empty)
  Copying to new object Graph(name=root, id140690800400160)

Calling __deepcopy__ for Graph(name=a, id140690800409808)
  Memo dictionary:
    Graph(name=root, id140690800410000): Graph(name=root, id140690800400160)
  Copying to new object Graph(name=a, id140690800399920)

Calling __deepcopy__ for Graph(name=root, id140690800410000)
  Already copied to (!r)

Calling __deepcopy__ for Graph(name=b, id140690800409184)
  Memo dictionary:
    Graph(name=root, id140690800410000): Graph(name=root, id140690800400160)
    Graph(name=a, id140690800409808): Graph(name=a, id140690800399920)
    140690800410000: Graph(name=root, id140690800400160)
    140690800498176: [Graph(name=root, id140690800410000), Graph(name=a, id140690800409808)]
    140690800409808: Graph(name=a, id140690800399920)
  Copying to new object Graph(name=b, id140690800399824)
'''
