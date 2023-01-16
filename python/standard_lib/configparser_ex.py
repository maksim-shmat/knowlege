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

#9 
