"""getopt about."""


#1 getop short

import getopt

'''
opts, args = getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')

for opt in opts:
    print(opt)

RESULTS:
('-a', '')
('-b', 'val')
('-c', 'val')
'''

#2 getopt long

import getopt

'''
opts, args = getopt.getopt(
        ['--noarg',
         '--witharg', 'val',
         '--witharg2=another'],
        '',
        ['noarg', 'witharg=', 'witharg2='],
)
for opt in opts:
    print(opt)

RESULTS:
('--noarg', '')
('--witharg', 'val')
('--witharg2', 'another')
'''

#3 getopt better fool example

import getopt
import sys

'''
version = '1.1'
verbose = False
output_filename = 'default.out'

print('ARGV    :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
            sys.argv[1:],
            'o:v',
            ['output=',
             'verbose',
             'version=',
             ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS  :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print('VERSION  :', version)
print('VERBOSE  :', verbose)
print('OUTPUT   :', output_filename)
print('REMAINING:', remainder)

RESULTS:  # with: $ python3 getopt_example.py -o foo
                 #$ python3 getopt_example.py -ofoo
                 #$ python3 getopt_example.py --output foo
                 #$ python3 getopt_example.py --output=foo
                 #$ python3 getopt_example.py --o foo
                 #$ python3 getopt_example.py --ver 2.0
#$ python3 getopt_example.py -v not_an_option --output foo

ARGV    : []
OPTIONS  : []
VERSION  : 1.1
VERBOSE  : False
OUTPUT   : default.out
REMAINING: []
'''

#4 getopt_gnu()

import getopt
import sys

'''
version = '1.0'
verbose = False
output_filename = 'default.out'

print('ARGV    :', sys.argv[1:])

try:
    options, remainder = getopt.gnu_getopt(
            sys.argv[1:],
            'o:v',
            ['output=',
             'verbose',
             'version=',
             ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS    :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print('VERSION    :', version)
print('VERBOSE    :', verbose)
print('OUTPUT     :', output_filename)
print('REMAINING  :', remainder)

# RESULTS with: $ python3 getopt_gnu.py -v not_an_option --output foo
'''
