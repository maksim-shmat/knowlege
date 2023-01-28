"""cgitb tests about."""

#1
'''
import cgitb
cgitb.enable(format='text')


def func2(a, divisor):
    return a / divisor

def func1(a, b):
    c = b - 5
    return func2(a, c)

func1(1, 5)
'''

#2 cgitb with classes
'''
import cgitb
cgitb.enable(format='text', context=12)


class BrokenClass:
    """It class contain error."""

    def __init__(self, a, b):
        """Will be worn with args this."""
        self.a = a
        self.b = b
        self.c = self.a * self.b
        # Ready
        # long
        # comment
        # goes
        # here.
        self.d = self.a / self.b
        return

o = BrokenClass(1, 0)
'''

#3 cgitb lob exception

import cgitb
import os


LOGDIR = os.path.join(os.path.dirname(__file__), 'LOGS_SHMOGS')

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)

cgitb.enable(
        logdir=LOGDIR,
        display=False,
        format='text',
)

def func(a, divisor):
    return a /divisor

func(1, 0)
