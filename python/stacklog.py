""" add to stack statistics data harvest. """
from stack2 import Stack

class StackLog(Stack):
    pushes = pops = 0
    def __init__(self, start=[]):
        self.maxlen = 0
        Stack.__init__(self, start)

    def push(self, object):
        Stack.push(self, object)
        StackLog.pushes += 1
        self.maxlen = max(self.maxlen, len(self))

    def pop(self):
        StackLog.pops += 1
        return Stack.pop(self)

    def stats(self):
        return self.maxlen, self.pushes, self.pops
"""
>from stacklog import StackLog
x = StackLog()
y = StackLog()
for i in range(3): x.push(i)
for c in 'spam': y.push(c)
>x, y
>y.pop(), x.pop()
>x.stats(), y.stats()
