"""atexit about."""

#1 atexit simple

import atexit

'''
def all_done():
    print('all_done()')

print('Registering')
atexit.register(all_done)
print('Registered')

RESULTS:
Registering
Registered
all_done()
'''

#2 atexit multiple

import atexit

'''
def my_cleanup(name):
    print('my_cleanup({})'.format(name))

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')

RESULTS:
my_cleanup(third)
my_cleanup(second)
my_cleanup(first)
'''

#3 atexit decorator

import atexit

'''
@atexit.register
def all_done():
    print('all_done()')

print('starting main program')

RESULTS:
starting main program
all_done()
'''

#4 atexit unregister

import atexit

'''
def my_cleanup(name):
    print('my_cleanup({})'.format(name))

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')

atexit.unregister(my_cleanup)
'''

#5 atexit unregister not registered

import atexit

'''
def my_cleanup(name):
    print('my_cleanup({})'.format(name))

if False:
    atexit.register(my_cleanup, 'never registered')

atexit.unregister(my_cleanup)
'''

#6 atexit signal parent  # for atexit_signal_child.py
# demonstrate how atexit work with signal

import os
import signal
import subprocess
import time

'''
proc = subprocess.Popen('./atexit_signal_child.py')
print('PARENT: Pausing before sending signal...')
time.sleep(1)
print('PARENT: Signaling child')
os.kill(proc.pid, signal.SIGTERM)
'''

#7 atexit os exit

import atexit
import os

'''
def not_called():
    print('This shoud not be called')

print('Registering')
atexit.register(not_called)
print('Registered')

print('Exiting...')
os._exit(0)

RESULTS:
Registering
Registered
Exiting...
'''

#8 atexit sys exit

import atexit
import sys

'''
def all_done():
    print('all_done()')
    print('Registering')
    atexit.register(all_done)
    print('Registered')

    print('Exiting...')
    sys.exit()
'''

#9 atexit exception

import atexit

'''
def exit_with_exception(message):
    raise RuntimeError(message)

atexit.register(exit_with_exception, 'Registered first')
atexit.register(exit_with_exception, 'Registered second')

RESULTS:
Exception ignored in atexit callback: <function exit_with_exception at 0x7f47ce6fbd90>
Traceback (most recent call last):
  File "<stdin>", line 144, in exit_with_exception
RuntimeError: Registered second
Exception ignored in atexit callback: <function exit_with_exception at 0x7f47ce6fbd90>
Traceback (most recent call last):
  File "<stdin>", line 144, in exit_with_exception
RuntimeError: Registered first
'''
