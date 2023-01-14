"""getpass about."""

#1 getpass defaults

import getpass

'''
try:
    p = getpass.getpass()
except Exception as err:
    print('ERROR:', err)
else:
    print('You entered:', p)
'''
#2 getpass prompt

import getpass

'''
p = getpass.getpass(prompt='What is your favorite color?')
if p.lower() == 'blue':
    print('Right. Off you go.')
else:
    print('Auuuuugh!')
'''

#3 getpass stream

import getpass
import sys

'''
p = getpass.getpass(stream=sys.stderr)
print('You entered:', p)
# python3 getpass_stream.py >/dev/null
'''

#4 getpass noterminal

import getpass
import sys


if sys.stdin.isatty():
    p = getpass.getpass('Using getpass: ')
else:
    print('Using readline')
    p = sys.stdin.readline().rstrip()

print('Read: ', p)
