"""os.path about."""

#1 os.path.split()

import os.path

PATHS = [
        '/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

'''RESULTS:
 '/one/two/three' : ('/one/two', 'three')
'/one/two/three/' : ('/one/two/three', '')
              '/' : ('/', '')
              '.' : ('', '.')
               '' : ('', '')
'''

#2 basename()

import os.path

PATHS = [
        '/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '',
]

for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))

'''RESULTS:
'/one/two/three' : 'three'
'/one/two/three/' : ''
              '/' : ''
              '.' : '.'
               '' : ''
'''

#3 dirname()

import os.path

PATHS = [
        '/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '',
]

for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.dirname(path)))

'''RESULTS:
'/one/two/three' : '/one/two'
'/one/two/three/' : '/one/two/three'
              '/' : '/'
              '.' : ''
               '' : ''
'''

#4 splittext()

import os.path

PATHS = [
        'filename.txt',
        'filename',
        '/path/to/filename.txt',
        '/',
        '',
        'my-archive.tar.gz',
        'no-extension.',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))

'''RESULTS:
'filename.txt' : ('filename', '.txt')
           'filename' : ('filename', '')
'/path/to/filename.txt' : ('/path/to/filename', '.txt')
                  '/' : ('/', '')
                   '' : ('', '')
  'my-archive.tar.gz' : ('my-archive.tar', '.gz')
      'no-extension.' : ('no-extension', '.')
'''

#5 commonprefix()

import os.path

paths = ['/one/two/three/four',
        '/one/two/threefold',
        '/one/two/three/',
        ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonprefix(paths))

'''RESULTS:
PATH: /one/two/three/four
PATH: /one/two/threefold
PATH: /one/two/three/

PREFIX: /one/two/three
'''

#6 commonpath()

import os.path

paths = ['/one/two/three/four',
        '/one/two/threefold',
        '/one/two/three/',
        ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))

'''RESULTS:
PATH: /one/two/three/four
PATH: /one/two/threefold
PATH: /one/two/three/

PREFIX: /one/two
'''

#7 join()

import os.path

PATHS = [
        ('one', 'two', 'three'),
        ('/', 'one', 'two', 'three'),
        ('/one', '/two', '/three'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))

'''RESULTS:
('one', 'two', 'three') : 'one/two/three'
('/', 'one', 'two', 'three') : '/one/two/three'
('/one', '/two', '/three') : '/three'
'''

#8 expanduser()

import os.path

for user in ['', 'dhellmann', 'nosuchuser']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.format(
        lookup, os.path.expanduser(lookup)))

'''RESULTS:
            '~' : '/home/joffrey'
   '~dhellmann' : '~dupa'
  '~nosuchuser' : '~nosuchuser'
'''

#9 expandvars()

import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print(os.path.expandvars('/path/to/$MYVAR'))

'''RESULTS:
/path/to/VALUE
'''

#10 normpath()

import os.path

PATHS = [
        'one//two//three',
        'one/./two/./three',
        'one/../alt/two/three',
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))

'''RESULTS:
     'one//two//three' : 'one/two/three'
   'one/./two/./three' : 'one/two/three'
'one/../alt/two/three' : 'alt/two/three'
'''

#11 abspath()

import os
import os.path

os.chdir('/usr')

PATHS = [
        '.',
        '..',
        './one/two/three',
        '../one/two/three',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))

'''RESULTS:
                  '.' : '/usr'
                 '..' : '/'
    './one/two/three' : '/usr/one/two/three'
   '../one/two/three' : '/one/two/three'
'''

#12 properties(), start from CLI
'''
import os.path
import time

print('File           :', __file__)
print('Access time    :', time.ctime(os.path.getatime(__file__)))
print('Modified time  :', time.ctime(os.path.getmtime(__file__)))
print('Change time    :', time.ctime(os.path.getctime(__file__)))
print('Size           :', os.path.getsize(__file__))

RESULTS:
    File           : /home/joffrey/djambGo12/nolege/python/standard_lib/os_path_ex.py
Access time    : Wed Oct 12 04:37:03 2022
Modified time  : Wed Oct 12 04:36:43 2022
Change time    : Wed Oct 12 04:36:43 2022
Size           : 4364
'''

#13 tests

import os.path

FILENAMES = [
        __file__,
        os.path.dirname(__file__),
        '/',
        './broken_link',
]

for file in FILENAMES:
    print('File        : {!r}'.format(file))
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Mountpoint? :', os.path.ismount(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    print()

#14
