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

import argparse

'''
parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('--optional', action="store_true",
                    default=False)
parser.add_argument('positional', action="store")

print(parser.parse_args())
'''

#17 argparse uses parent with group

import argparse
#import argparse_parent_with_group

'''
parser = argparse.ArgumentParser(
        parent = [argparse_parent_with_group.parser],
)

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
'''

#18 argparse mutually exclusive

import argparse

'''
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

print(parser.parse_args())

RESULTS: with: $ python3 argparse_mutually_exclusive.py -a
         Namespace(a=True, b=False)

         with: $ python3 argparse_mutually_exclusive.py -b
         Namespace(a=False, b=True)

         with: $ python3 argparse_mutually_exclusive.py -a -b
         usage: argparse_mutually_exclusive.py [-h] [-a | -b]
         argparse_mutually_exclusive.py: error: argument -b: not allowed
         with argument -a
# either -a either -b
'''

#19 argparse subparser

import argparse

'''
parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# list command
list_parser = subparsers.add_parser(
        'list', help='List contents')
list_parser.add_argument(
        'dirname', action='store',
        help='Directory to list')

# create command
create_parser = subparsers.add_parser(
        'create', help='Create a directory')
create_parser.add_argument(
        'dirname', action='store',
        help='New directory to create')
create_parser.add_argument(
        '--read-only', default=False, action='store_true',
        help='Set permissions to prevent writing to the directory',
)

# delete command
delete_parser = subparsers.add_parser(
        'delete', help='Remove a directory')
delete_parser.add_argument(
        'dirname', action='store', help='The directory to remove')
delete_parser.add_argument(
        '--recursive', '-r', default=False, action='store_true',
        help='Remove the contents of the directory, too',
)

print(parser.parse_args())

# python3 argparse_subparsers.py -h
'''

#20 argparse nargs

import argparse

'''
parser = argparse.ArgumentParser()

parser.add_argument('--three', nargs=3)

parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more', nargs='+')

print(parser.parse_args())

# $ python3 argparse_nargs.py -h
'''

#21 argparse type

import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-i', type=int)
parser.add_argument('-f', type=float)
parser.add_argument('--file', type=open)

try:
    print(parser.parse_args())
except IOError as msg:
    parser.error(str(msg))

# $ python3 argparse_type.py -i 1
# $ python3 argparse_type.py -f 3.14
# $ python3 argparse_type.py --file argparse_type.py


#22 argparse choices

import argparse

'''
parser = argparse.ArgumentParser()

parser.add_argument(
        '--mode',
        choices=('read-only', 'read-write')
)

print(parser.parse_args())
'''
# $ python3 argparse_choices.py -h
# $ python3 argparse_choices.py --mode read-only
# $ python3 argparse_choices.py --mode invalid

#23 argparse FileType

import argparse

'''
parser = argparse.ArgumentParser()

parser.add_argument('-i', metavar='in-file',
                    type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file',
                    type=argparse.FileType('wt'))

try:
    results = parser.parse_args()
    print('Input file:', results.i)
    print('Output file:', results.o)
except IOError as msg:
    parser.error(str(msg))
'''
# $ python3 argparse_FileType.py -h
# $ python3 argparse_FileType.py -i argparse_FileType.py -o tmp_file.txt
# $ python3 argparse_FileType.py -i no_such_file.txt

#24 argparse custom action

import argparse

'''
class CustomAction(argparse.Action):
    
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        print('Initializing CustomAction')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print('{} = {!r}'.format(name, value))
        print()
        return

    def __call__(self, parser, namespace, values,
                 option_string=None):
        print('Processing CustomAction for {}'.format(self.dest))
        print('  parser = {}'.format(id(parser)))
        print('  values = {!r}'.format(values))
        print('  option_strng = {!r}'.format(option_string))

        # Handle 
        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        # Save results in area of names with destination for constructor
        setattr(namespace, self.dest, values)
        print()

parser = argparse.ArgumentParser()

parser.add_argument('-a', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)

results = parser.parse_args(['-a', 'value',
                             '-m', 'multivalue',
                             'second'])
print(results)

RESULTS:
Namespace(i=None, f=None, file=None)
Initializing CustomAction
dest = 'a'
option_strings = ['-a']
required = False

Initializing CustomAction
dest = 'm'
nargs = '*'
option_strings = ['-m']
required = False

Processing CustomAction for a
  parser = 139983794005200
  values = 'value'
  option_strng = '-a'

Processing CustomAction for m
  parser = 139983794005200
  values = ['multivalue', 'second']
  option_strng = '-m'

Namespace(a='VALUE', m=['MULTIVALUE', 'SECOND'])
'''
