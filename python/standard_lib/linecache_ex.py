"""Work with linecache"""

import this

#1 getline()

import linecache
from linecache_data import *

filename = make_tempfile()

# get string from file and from cache

# linecache named strings from 1 against 0 by Python default

print('SOURCE:')
print('{!r}'.format(lorem.split('\n')[4]))  # from 0
print()
print('CACHE:')
print('{!r}'.format(linecache.getline(filename, 5))) # from 1

cleanup(filename)

'''RESULTS:
SOURCE:
'fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur'

CACHE:
'fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur\n'
'''

#2 check empty line

import linecache
from linecache_data import *

filename = make_tempfile()

print()
# Empty strings include \n
print('BLANK: {!r}'.format(linecache.getline(filename, 8)))

cleanup(filename)

'''RESULTS:
BLANK: '\n'
'''

#3 linecache out of range

import linecache
from linecache_data import *

filename = make_tempfile()

# if string not exist linecache return empty string
not_there = linecache.getline(filename, 500)
print('NOT THERE: {!r} includes {} characters'.format(
    not_there, len(not_there)))

cleanup(filename)

'''RESULTS:
NOT THERE: '' includes 0 characters
'''

#4 missing file

import linecache

no_such_file = linecache.getline(
        'this_file_does_not_exist.txt', 1,
)
print('NO FILE: {!r}'.format(no_such_file))

'''RESULTS:
NO FILE: ''
'''

#5 linecache path search

import linecache
import os

module_line = linecache.getline('linecache.py', 3)
print('MODULE:')
print(repr(module_line))

file_src = linecache.__file__
if file_src.endswith('.pyc'):
    file_src = file_src[:-1]
print('\nFILE:')
with open(file_src, 'r') as f:
    file_line = f.readlines()[2]
print(repr(file_line))

'''RESULTS:
MODULE:
'This is intended to read lines from modules imported -- hence if a filename\n'

FILE:
'This is intended to read lines from modules imported -- hence if a filename\n'
'''
