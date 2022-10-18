'''glob module about.'''

#1 

import glob

for name in sorted(glob.glob('../*')):  # in previous dir any files
    print(name)

#2

import glob

print('Named explicitly:')
for name in sorted(glob.glob('./../*')):
    print(' {}'.format(name))

print('Named with wildcard:')
for name in sorted(glob.glob('./*/*')):
    print(' {}'.format(name))

#3 <?>
import glob

print()
for name in sorted(glob.glob('./*?.txt')):
    print(name)

#4 for number before .txt

import glob

for name in sorted(glob.glob('dir/*[0-9].*')):
    print(name)

#5 escape()

import glob

specials = '?*['

for char in specials:
    pattern = 'dir/*' + glob.escape(char) + '.txt'
    print('Searching for: {!r}'.format(pattern))
    for name in sorted(glob.glob(pattern)):
        print(name)
    print()
