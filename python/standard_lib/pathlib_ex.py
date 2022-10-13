"""Pathlib about."""

#1 pathlib operator

import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr/'local'
print(usr_local)

usr_share = usr/pathlib.PurePosixPath('share')
print(usr_share)

root = usr/'..'
print(root)

etc = root/'/etc/'
print(etc)

'''RESULTS:
/usr
/usr/local
/usr/share
/usr/..
/etc
'''

#2 resolve()

import pathlib

print()
usr_local = pathlib.Path('/usr/local')
share = usr_local/'..'/'share'
print(share.resolve())

'''RESULTS:
/usr/share
'''

#3 joinpath()

import pathlib

print()
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)

'''RESULTS:
/usr/local
'''

#4 pathlib from existing, with with_name() and with_suffix()

import pathlib

ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)

py = ind.with_name('pathlib_from_existing.py')
print(py)

pyc = py.with_suffix('.pyc')
print(pyc)

'''RESULTS:
source/pathlib/index.rst
source/pathlib/pathlib_from_existing.py
source/pathlib/pathlib_from_existing.pyc
'''

#5 pathlib parts

import pathlib

p = pathlib.PurePosixPath('/usr/local')
print(p.parts)

'''RESULTS:
('/', 'usr', 'local')
'''

#6 parents

import pathlib

print()
p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)

'''RESULTS:
parent: /usr/local

hierarchy:
/usr/local
/usr
/
'''

#7 name, suffix, stem

import pathlib

p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print()
print('path  : {}'.format(p))
print('name  : {}'.format(p.name))
print('suffix: {}'.format(p.suffix))
print('stem  : {}'.format(p.stem))

'''RESULTS:
path  : source/pathlib/pathlib_name.py
name  : pathlib_name.py
suffix: .py
stem  : pathlib_name
'''

#8 convinience
