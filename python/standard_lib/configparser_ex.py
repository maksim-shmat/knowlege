"""configparser about."""

#1 Simple configfile simple.ini
'''
# simple example
[bug_tracker]
url = http://localhost:8080/bugs/
ursername = dhellhound
; Don`t keep passwords into simple text configurational files!
password = SECRET
'''

#2 configparser read

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))
'''

#3 configparser read many

from configparser import ConfigParser
import glob

'''
parser = ConfigParser()

candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
              'simple.ini', 'multisection.ini']

found = parser.read(candidates)

missing = set(candidates) - set(found)

print('Found config files:', sorted(found))
print('Missing files     :', sorted(missing))
'''

#4 configparser import ConfigParser

import codecs

'''
parser = ConfigParser()
parser.read('unicode.ini', encoding='utf-8')

password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Type    :', type(password))
print('repr()  :', repr(password))
'''

#5 configparser structure  # for  multisection.ini

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('multisection.ini')

for section_name in parser.sections():
    print('Section:', section_name)
    print('Options:', parser.options(section_name))
    for name, value in parser.items(section_name):
        print('  {} = {}'.format(name, value))
    print()

RESULTS:
Section: bug_tracker
Options: ['url', 'username', 'password']
  url = http://localhost:8080/bugs/
  username = dhellhound
  password = SECRET

Section: wiki
Options: ['url', 'username', 'password']
  url = http://localhost:8080/wiki/
  username = dhellhound
  password = SECRET
'''

#6 configparser structure dict

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('multisection.ini')

for section_name in parser:
    print('Section:', section_name)
    section = parser[section_name]
    print('  Options:', list(section.keys()))
    for name in section:
        print('  {} = {}'.format(name, section[name]))
    print()

RESULTS:
Section: DEFAULT
  Options: []

Section: bug_tracker
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/bugs/
  username = dhellhound
  password = SECRET

Section: wiki
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/wiki/
  username = dhellhound
  password = SECRET
'''

#7 configparser has section

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('multisection.ini')

for candidate in ['wiki', 'bug_tracker', 'dvcs']:
    print('{:<12}: {}'.format(
        candidate, parser.has_section(candidate)))

RESULTS:
wiki        : True
bug_tracker : True
dvcs        : False
'''

#8 configparser has option

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('multisection.ini')

SECTIONS = ['wiki', 'none']
OPTIONS = ['username', 'password', 'url', 'description']

for section in SECTIONS:
    has_section = parser.has_section(section)
    print('{} section exists: {}'.format(section, has_section))
    for candidate in OPTIONS:
        has_option = parser.has_option(section, candidate)
        print('{}.{:<12}  : {}'.format(
            section, candidate, has_option))
        print()

RESULTS:
wiki section exists: True
wiki.username      : True

wiki.password      : True

wiki.url           : True

wiki.description   : False

none section exists: False
none.username      : False

none.password      : False

none.url           : False

none.description   : False
'''

#9 configparser value types, for types.ini

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('types.ini')

print('Integers:')
for name in parser.options('ints'):
    string_value = parser.get('ints', name)
    value = parser.getint('ints', name)
    print('  {:<12} : {!r:<7} -> {}'.format(
        name, string_value, value))

print('\nFloats:')
for name in parser.options('floats'):
    string_value = parser.get('floats', name)
    value = parser.getfloat('floats', name)
    print('  {:<12} : {!r:<7} -> {:0.2f}'.format(
        name, string_value, value))

print('\nBooleans:')
for name in parser.options('booleans'):
    string_value = parser.get('booleans', name)
    value = parser.getboolean('booleans', name)
    print('  {:<12} : {!r:<7} -> {}'.format(
        name, string_value, value))

RESULTS:
Integers:
  positive     : '1'     -> 1
  negative     : '-5'    -> -5

Floats:
  positive     : '0.2'   -> 0.20
  negative     : '-3.14' -> -3.14

Booleans:
  number_true  : '1'     -> True
  number_false : '0'     -> False
  yn_true      : 'yes'   -> True
  yn_false     : 'no'    -> False
  tf_true      : 'true'  -> True
  tr_false     : 'false' -> False
  onoff_true   : 'on'    -> True
  onoff_false  : 'false' -> False
'''

#10 configparser custom types

from configparser import ConfigParser
import datetime

'''
def parse_iso_datetime(s):
    print('parse_iso_datetime({!r})'.format(s))
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f')

parser = ConfigParser(
        converters={
            'datetime': parse_iso_datetime,
        }
)
parser.read('custom_types.ini')

string_value = parser['datetimes']['due_date']
value = parser.getdatetime('datetimes', 'due_date')
print('duei_date : {!r} -> {!r}'.format(string_value, value))
'''

#11 configparser allow no value

import configparser

'''
try:
    parser = configparser.ConfigParser()
    parser.read('allow_no_value.ini')
except configparser.ParsingError as err:
    print('Could not parse:', err)

# Allow use parameters without values
print('\nTrying again with allow_no_value=True')
parser = configparser.ConfigParser(allow_no_value=True)
parser.read('allow_no_value.ini')
for flag in ['turn_feature_on', 'turn_other_feature_on']:
    print('\n', flag)
    exists = parser.has_option('flags', flag)
    print('  has_option:', exists)
    if exists:
        print('    get:', parser.get('flags', flag))
'''

#12 configparser populate

import configparser

'''
parser = configparser.SafeConfigParser()

parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'deadhound')
parser.set('bug_tracker', 'password', 'secret')

for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print('  {} = {!r}'.format(name, value))

RESULTS:
<stdin>:277: DeprecationWarning: The SafeConfigParser class has been renamed to ConfigParser in Python 3.2. This alias will be removed in Python 3.12. Use ConfigParser directly instead.
bug_tracker
  url = 'http://localhost:8080/bugs'
  username = 'deadhound'
  password = 'secret'
'''

#13 configparser remove

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('multisection.ini')

print('Read values:\n')
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print('  {} = {!r}'.format(name, value))

parser.remove_option('bug_tracker', 'password')
parser.remove_section('wiki')

print('\nModified values:\n')
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print('  {} = {!r}'.format(name, value))

RESULTS:
Read values:

bug_tracker
  url = 'http://localhost:8080/bugs/'
  username = 'dhellhound'
  password = 'SECRET'
wiki
  url = 'http://localhost:8080/wiki/'
  username = 'dhellhound'
  password = 'SECRET'

Modified values:

bug_tracker
  url = 'http://localhost:8080/bugs/'
  username = 'dhellhound'
'''

#14 configparser write

import configparser
import sys

'''
parser = configparser.ConfigParser()

parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'dhellhound')
parser.set('bug_tracker', 'password', 'secret')

parser.write(sys.stdout)

RESULTS:
:w !python3
[bug_tracker]
url = http://localhost:8080/bugs
username = dhellhound
password = secret

# After read and second write comments will be autoremove
'''

#15 configparser defaults
# Need tests

import configparser

'''
# Definite names of parameters
option_names = [
        'from-default',
        'from-section', 'section-only',
        'file-only', 'init-only', 'init-and-file',
        'from-vars',
]

# Init analizator with row of default values
DEFAULTS = {
        'from-default': 'value from defaults passed to init',
        'init-only': 'value from defaults passed to init',
        'init-and-file': 'value from defaults passed to init',
        'from-section': 'value from defaults passed to init',
        'from-vars': 'value from defaults passed to init',
}
parser = configparser.ConfigParser(defaults=DEFAULTS)

print('Defaults before loading file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('  {:<15} = {!r}'.format(name, defaults[name]))

# Load config file
parser.read('with-defaults.ini')

print('\nDefaults after loading file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('  {:<15} = {!r}'.format(name, defaults[name]))

# Redefinite row of local values?
vars = {'from-vars': 'value from vars'}

# Show values of all parameters
print('\nOption lookup:')
for name in option_names:
    value = parser.get('sect', name, vars=vars)
    print('  {:<15} = {!r}'.format(name, value))

# Show error messages for not exists parameters
print('\nError cases:')
try:
    print('No such option:', parser.get('sect', 'no-option'))
except configparser.NoOptionError as err:
    print(err)

try:
    print('No such section:', parser.get('no-sect', 'no-option'))
except configparser.NoSectionError as err:
    print(err)
'''

#16 configparser interpolation

import configparser

'''
parser = configparser.ConfigParser()
parser.read('interpolation.ini')

parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url',
           'http://%(server)s:%(port)s/bugs')

try:
    print(parser.get('bug_tracker', 'url'))
except configparser.InterpolationMissingOptionError as err:
    print('ERROR:', err)

RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 432, in <module>
  File "/usr/lib/python3.10/configparser.py", line 1212, in add_section
    super().add_section(section)
  File "/usr/lib/python3.10/configparser.py", line 659, in add_section
    raise DuplicateSectionError(section)
configparser.DuplicateSectionError: Section 'bug_tracker' already exists

EXPECTED RESULTS:
    Original value    : http://localhost:8080/bugs/
    Altered port value: http://localhost:9090/bugs/
    Without interpolation: %(protocol)s://%(server)s:%(port)s/bugs/
'''

#17 configparser interpolation defaults

from configparser import ConfigParser

'''
parser = ConfigParser()
parser.read('interpolation_defaults.ini')

print('URL:', parser.get('bug_tracker', 'url'))

RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 465, in <module>
  File "/usr/lib/python3.10/configparser.py", line 782, in get
    d = self._unify_values(section, vars)
  File "/usr/lib/python3.10/configparser.py", line 1153, in _unify_values
    raise NoSectionError(section) from None
configparser.NoSectionError: No section: 'bug_tracker'
'''

#18 configparser interpolation recursion

import configparser

'''
parser = configparser.ConfigParser()

parser.add_section('sect')
parser.set('sect', 'opt', '%(opt)s')

try:
    print(parser.get('sect', 'opt'))
except configparser.InterpolationDepthError as err:
    print('ERROR:', err)

RESULTS:  # norm
ERROR: Recursion limit exceeded in value substitution: option 'opt' in section 'sect' contains an interpolation key which cannot be substituted in 10 steps. Raw value: '%(opt)s'
'''

#19 configparser escape  # spesial symbols

# into file .ini write: [escape]
#                       value = a literal %% most be escaped
from configparser import ConfigParser
import os

'''
filename = 'escape.ini'
config = ConfigParser()
config.read([filename])

value = config.get('escape', 'value')

print(value)

RESULTS:
    a literal % must be escaped
'''

#20 configparser extendedinterpolation

from configparser import ConfigParser, ExtendedInterpolation

'''
parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read('extended_interpolation.ini')

print('Original value    :', parser.get('bug_tracker', 'url'))

parser.set('intranet', 'port', '9000')
print('Altered port value:', parser.get('bug_tracker', 'url',
                                        raw=True))

RESULTS:
Original value    : http://localhost:8080/bugs/
Altered port value: http://${intranet:server}:${intranet:port}/bugs/
'''

#21 configparser nointerpolation
