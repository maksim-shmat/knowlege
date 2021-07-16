""" Optimisation for use the tree tuples. """
class Stack:
    def __init__(self, start=[]):
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i - 1])

    def push(self, node):
        self.stack = node, self.stack

    def empty(self):
        return not self.stack

    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len, tree = len+1, tree[1]
        return len

    def __getitem__(self, index):
        len, tree = 0, self.stack
        while len < index and tree:
            len, tree = len+1, tree[1]
        if tree:
            return tree[0]
        else:
            raise IndexError()

    def __repr__(self):
        return '[FastStack:' + repr(self.stack) + ']'

"""
>from stack3 import Stack
x = Stack()
y = Stack()
for c in 'spam': x.push(c)
for i in range(3): y.push(i)
x
y
len(x), x[2], x[-1]
x.pop()
x
while y: print(y.pop(), end=' ')
"""
