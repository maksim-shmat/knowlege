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

#12 
