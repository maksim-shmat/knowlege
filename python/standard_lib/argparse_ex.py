"""argparse about."""

#1 argparse short

import argparse

'''
parser = argparse.ArgumentParser(description="Short sample app")
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['-a', '-bval', '-c', '3']))

RESULTS:
Namespace(a=True, b='val', c=3)
'''

#2 argparse long

import argparse

'''
parser = argparse.ArgumentParser(
        description='Example with long option names',
)
parser.add_argument('--noarg', action="store_true",
                    default=False)
parser.add_argument('--withard', action="store",
                    dest="withard")
parser.add_argument('--withard2', action="store",
                    dest="withard2", type=int)

print(parser.parse_args(['--noarg', '--withard', 'val', '--withard2=3']))

RESULTS:
Namespace(noarg=True, withard='val', withard2=3)
'''

#3 argparse arguments

import argparse

'''
parser = argparse.ArgumentParser(
        description='Example with nonoptional arguments',
)

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print(parser.parse_args())

RESULTS:
usage: [-h] count units
: error: the following arguments are required: count, units
'''

#4 argparse action

import argparse

'''
parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store',
                    dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const',
                    dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')

parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Set a switch to false')

parser.add_argument('-a', action='append',
                    dest='collection',
                    default=[],
                    help='Add repeated value to a list')

parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')

parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value    = {!r}'.format(results.simple_value))
print('constant_value  = {!r}'.format(results.constant_value))
print('boolean_t       = {!r}'.format(results.boolean_t))
print('boolean_f       = {!r}'.format(results.boolean_f))
print('collection      = {!r}'.format(results.collection))
print('const_collection = {!r}'.format(rsults.const_collection))
    
RESULTS: with: $ python3 argparse_action.py -h
               $ python3 argparse_action.py -s value
               $ python3 argparse_action.py -c
               $ python3 argparse_action.py -t
               $ python3 argparse_action.py -f
               $ python3 argparse_action.py -a one -a two -a three
               $ python3 argparse_action.py -B -A
               $ python3 argparse_action.py --version
'''

#5 argparse prefix chars

import argparse

'''
parser = argparse.ArgumentParser(
        description='Change the option prefix characters',
        prefix_chars='-+/',
)

parser.add_argument('-a', action="store_false",
                    default=None,
                    help='Turn A off',
                    )
parser.add_argument('+a', action="store_true",
                    default=None,
                    help='Turn A on',
                    )
parser.add_argument('//noarg', '++noarg',
                    action="store.true",
                    default=False)

print(parser.parse_args())

RESULTS: with: $ python3 argparse_prefix_chars.py -h
               $ python3 argparse_prefix_chars.py +a
               $ python3 argparse_prefix_chars.py -a
               $ python3 argparse_prefix_chars.py //noarg
               $ python3 argparse_prefix_chars.py ++noarg
               $ python3 argparse_prefix_chars.py --noarg
'''

#6 argparse with shlex

# need file configparser with note: [cli]
#                                   options = -a -b 2

import argparse
from configparser import ConfigParser
import shlex

'''
parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_with_shlex.ini')
config_value = config.get('cli', 'options')
print('Config  :', config_value)

argument_list = shlex.split(config_value)
print('Arg List:', argument_list)

print('Results :', parser.parse_args(argument_list))
'''

#7 argparse fromfile prefix chars
# need file argparse_fromfile_prefix_chars.txt with: -a
#                                                    -b
#                                                    2

import argparse
import shlex

'''
parser = argparse.ArgumentParser(description='Short sample app',
                                 fromfile_prefix_chars='@',
                                 )
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['@argparse_fromfile_prefix_chars.txt']))
'''

#8 argparse with help

import argparse

'''
parser = argparse.ArgumentParser(add_help=True)  # or False fof off help

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args())

RESULTS:
Namespace(a=False, b=None, c=None)
'''

#9 argparse custom help

import argparse

'''
parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print('print_usage output:')

parser.print_usage()
print()

print('print_help output:')
parser.print_help()

RESULTS:
print_usage output:
usage: [-h] [-a] [-b B] [-c C]

print_help output:
usage: [-h] [-a] [-b B] [-c C]

options:
  -h, --help  show this help message and exit
  -a
  -b B
  -c C
'''

#10 argparse raw description help formatter

import argparse

'''
parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        description
            not
                wrapped""",
        epilog="""
        epilog
            not
                wrapped""",
)

parser.add_argument(
        '-a', action="store_true",
        help="""argument
        help is
        wrapped
        """,
)

parser.print_help()

RESULTS:
usage: [-h] [-a]

        description
            not
                wrapped

options:
  -h, --help  show this help message and exit
  -a          argument help is wrapped

        epilog
            not
                wrapped
'''

#11 argparse raw text help formatter

import argparse

'''
parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
        description
            not
                wrapped""",
        epilog="""
        epilog
            not
                werapped""",
)

parser.add_argument(
        '-a', action="store_true",
        help="""argument
        help is not
        wrapped
        """,
)

parser.print_help()

RESULTS:
usage: [-h] [-a]

        description
            not
                wrapped

options:
  -h, --help  show this help message and exit
  -a          argument
                      help is not  # <-
                      wrapped      # <-
                      

        epilog
            not
                werapped
'''

#12 argparse metavar type help formatter

import argparse

'''
parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.MetavarTypeHelpFormatter,
)

parser.add_argument('-i', type=int, dest='notshown1')
parser.add_argument('-f', type=float, dest='notshown2')

parser.print_help()

RESULTS:
usage: [-h] [-i int] [-f float]

options:
  -h, --help  show this help message and exit
  -i int
  -f float
'''

#13 argparse parent base

import argparse

'''
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--user', action="store")
parser.add_argument('--password', action="store")

#13.1 argparse uses parent

import argparse
import argparse_parent_base


parser = argparse.ArgumentParser(
        parents=[argparse_parent_base.parent],
)

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)
print(parser.parse_args())
'''

#14 argparse conflict handler resolve

import argparse

'''
parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('-b', action="store", help='Short alone')
parser.add_argument('--long-b', '-b',
                    action="store",
                    help='Long and short together')

print(parser.parse_args(['-h']))

RESULTS:
usage: [-h] [-a A] [--long-b LONG_B]

options:
  -h, --help            show this help message and exit
  -a A
  --long-b LONG_B, -b LONG_B
                        Long and short together
'''

#15 argparse conflict handler resolve2

import argparse

'''
parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('--long-b','-b',
                    action="store",
                    help='Long and short together')
parser.add_argument('-b', action="store", help='Short alone')

print(parser.parse_args(['-h']))

RESULTS:
usage: [-h] [-a A] [--long-b LONG_B] [-b B]

options:
  -h, --help       show this help message and exit
  -a A
  --long-b LONG_B  Long and short together  # <-
  -b B             Short alone
'''

#16 argparse default grouping
