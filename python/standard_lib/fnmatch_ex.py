"""fnmatch module about."""

#1

import fnmatch
import os

pattern = 'jill*.txt'
print('Pattern :', pattern)
print()
files = os.listdir('.')
for name in files:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))

#2 for find in a REGISTER use fnmatchcase()

import fnmatch
import os

pattern = 'JILL*.PY'
print('Pattern:', pattern)
print()

files = os.listdir('.')

for name in files:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatchcase(name, pattern)))

#3 filter()

import fnmatch
import os
import pprint

pattern = 'clare*.py'
print('Pattern :', pattern)

files = os.listdir('.')

print('\nFiles :')
pprint.pprint(files)

print('\nMatches :')
pprint.pprint(fnmatch.filter(files, pattern))

'''RESULTS:
Matches :
['clare.py']
'''

#4 glob to re with translate()

import fnmatch

pattern = 'clare*.py'
print('Pattern:', pattern)
print('Regex  :', fnmatch.translate(pattern))

'''RESULTS:
Pattern: clare*.py
Regex  : (?s:clare.*\.py)\Z
'''
