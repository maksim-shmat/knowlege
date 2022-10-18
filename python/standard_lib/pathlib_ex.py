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

import pathlib

home = pathlib.Path.home()
print('home: ', home)

cwd = pathlib.Path.cwd()
print('cwd :', cwd)

'''RESULTS:
home:  /home/jack
cwd : /home/jack/django2/knowlege/python/standard_lib
'''

#9 iterdir()

import pathlib

p = pathlib.Path('.')

for f in p.iterdir():
    print(f)

'''RESULTS:
names all files in dir
'''

#10 glob() for pattern

import pathlib

print()
p = pathlib.Path('..')

for f in p.glob('*.dat'):
    print(f)

'''RESULTS:
not show files in . dir, but show another
'''

#11 rglob() or **

import pathlib

print()
p = pathlib.Path('..')

for f in p.rglob('pathlib_*.py'):
    print(f)

'''RESUlTS:
../standard_lib/pathlib_ex.py
'''

#12 read_bytes(), read_text(), write_bytes() write_text(), open()

import pathlib

f = pathlib.Path('example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print('read from open(): {!r}'.format(handle.read()))

print('read_text(): {!r}'.format(f.read_text('utf-8')))

'''RESULTS:
read from open(): 'This is the content'
read_text(): 'This is the content'
'''

#13 test types of files

import itertools
import os
import pathlib

root = pathlib.Path('test_files')

if root.exists():
    for f in root.iterdir():
        f.unlink()
    else:
        root.mkdir()

    # Make a test file
    (root/'symlink').symlink_to('file')
    os.mkfifo(str(root/'fifo'))

    # test types of files
    to_scan = itertools.chain(
            root.itertir(),
            [pathlib.Path('/dev/disc0'),
                pathlib.Path('/dev/console')],
    )
    hfmt = '{:18s}'+('{!r:?5}'*6)
    for f in to_scan:
        print(fmt.format(
            str(f),
            f.is_file(),
            f.is_dir(),
            f.is_symlink(),
            f.is_fifo(),
            f.is_block_device(),
            f.is_char_device(),
        ))

'''RESULTS:
----
but it's may be that:
Name                    File   Dir    Link   FIFO   BLock  Character
test_files/fifo         False  False  False  True   False  False
test_files/file         True   False  False  False  False  False
test_files/symlink      True   False  True   False  False  False
/dev/disk0              Fasle  False  False  False  True   False
/dev/console            False  False  False  False  False  True
'''

#14 ownership

import pathlib

p = pathlib.Path('clare.py')

print()
print('{} is owned by {}/{}'.format(p, p.owner(), p.group()))

'''RESULTS:
clare.py is owned by jack/jack
'''

#15 touch()

import pathlib
import time

print()
p = pathlib.Path('clare.py')
if p.exists():
    print('already exists')
else:
    print('creating new')

p.touch()
start = p.stat()

time.sleep(1)

p.touch()
end = p.stat()

print('Start:', time.ctime(start.st_mtime))
print('End  :', time.ctime(end.st_mtime))

'''RESULTS:
creating new
...

already exists
Start: Mon Oct 17 04:31:55 2022
End  : Mon Oct 17 04:31:56 2022
'''

#16 chmod()

import os
import pathlib
import stat

f = pathlib.Path('pathlib_chmod_example.txt')
if f.exists():
    f.unlink()
f.write_text('contents')

# check permissions with stat
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print('Before: {:o}'.format(existing_permissions))

# how we change it
if not (existing_permissions & os.X_OK):
    print('Adding execute permission')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # use xor
    new_permissions = existing_permissions ^ stat.S_IXUSR

# make new permission
f.chmod(new_permissions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print('After: {:o}'.format(after_permissions))

'''RESULTS:
Before: 664
Adding execute permission
After: 764
'''
