"""shutil about."""

#1 copyfile()

import glob
import shutil

print('BEFORE:', glob.glob('clare.*'))

shutil.copyfile('clare.py', 'clare.py.copy')
print('AFTER:', glob.glob('clare.*'))

#2 copyfileobj()

import io
import os
import shutil
import sys

class VerboseStringIO(io.StringIO):

    def read(self, n=-1):         # -1 means read all input data
        next = io.StringIO.read(self, n)
        print('read({}) got {} bytes'.format(n, len(next)))
        return next


lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vestibulum aliquam mollis dolor. Donec
vulputate nunc ut diam. Ut rutrum mi vel sem. Vestibulum
ante ipsum.'''

print('Default:')
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output)

print()

print('All at once:')
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output, -1)

print()

print('Block of 256:')
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input,output, 256)

'''RESULTS:
Default:
read(65536) got 165 bytes
read(65536) got 0 bytes

All at once:
read(-1) got 165 bytes
read(-1) got 0 bytes

Block of 256:
read(256) got 165 bytes
read(256) got 0 bytes
'''

#3 copytree()

'''
import glob
import pprint
import shutil

print'BEFORE:')
pprint.pprint(glob.glob('/tmp/example/*'))

shutil.copytree('../shutil', '/tmp/example')

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))

#4 copytree() verbose

import glob
import pprint
import shutil

def vervose_copy(src, dst):
    print('copyin\n {!r}\n to {!r}'.format(src, dst))
    return shutil.copy2(src, dst)

print('BEFORE:')
pprint.pprint(glob.glob('/tmp/example/*'))
print()

shutil.copytree(
        '../shutil', '/tmp/example',
        copy_function=verbose_copy,
        ignore=shutil.ignore_patterns('*.py'),
)

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))

#5 rmtree()

import glob
import pprint
import shutil

print('BEFORE:')
pprint.pprint(glob.glob('/tmp/example/*'))

shutil.rmtree('/tmp/example')  # add to second agrs True for ignore errors

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))

#6 move()

import glob
import shutil

with open('example.txt', 'wt') as f:
    f.write('contents')

print('BEFORE: ', glob.glob('example*'))

shutil.move('example.txt', 'example.out')

print('AFTER: ', glob.glob('example*'))
'''

#7 which()

import shutil

print(shutil.which('virtualenv'))
print(shutil.which('tox'))
print(shutil.which('no-such-program'))

'''RESULTS:
/home/jack/.local/bin/virtualenv
None
None
'''

#8 which() for regular file

import os
import shutil

print()
path = os.pathsep.join([
    '.',
    os.path.expanduser('~/django2/knowlege/python'),
])  # default os.environ('PATH')

mode = os.F_OK | os.R_OK

filename = shutil.which(
        'jill.py',
        mode=mode,
        path=path,
)

print(filename)

'''RESULTS:
/home/jack/django2/knowlege/python/jill.py
'''

#9 get_archive_formats()

import shutil

for format, description in shutil.get_archive_formats():
    print('{:<5}: {}'.format(format, description))

'''RESULTS:
bztar: bzip2'ed tar-file
gztar: gzip'ed tar-file
tar  : uncompressed tar file
xztar: xz'ed tar-file
zip  : ZIP file
'''

#10 make archive

import logging
import shutil
import sys
import tarfile

logging.basicConfig(
        format='%(message)s',
        stream=sys.stdout,
        level=logging.DEBUG,
)
logger = logging.getLogger('pymotw')

print('Creating archive:')
shutil.make_archive(
        'example', 'gztar',
        root_dir='..',
        base_dir='shutil',
        logger=logger,
)

print('\nArchive contents:')
with tarfile.open('example.tar.gz', 'r') as t:
    for n in t.getnames():
        print(n)

#11 get_unpack_formats()

import shutil

for format, exts, description in shutil.get_unpack_formats():
    print('{:<5}: {}, names ending in {}'.format(
        format, description, exts))

'''RESULTS:
bztar: bzip2'ed tar-file, names ending in ['.tar.bz2', '.tbz2']
gztar: gzip'ed tar-file, names ending in ['.tar.gz', '.tgz']
tar  : uncompressed tar file, names ending in ['.tar']
xztar: xz'ed tar-file, names ending in ['.tar.xz', '.txz']
zip  : ZIP file, names ending in ['.zip']
'''

#12 uhpack_archive

import pathlib
import shutil
import sys
import tempfile

with tempfile.TemporaryDirectory() as d:
    print('Unpacking archive:')
    shutil.unpack_archive(
            'example.tar.gz',
            extract_dir=d,
    )

    print('\nCreated:')
    prefix_len = len(d) + 1
    for extracted in pathlib.Path(d).rglob('*'):
        print(str(extracted)[prefix_len:])

'''RESULTS:
Unpacking archive:

Created:
shutil
'''

#13 shutil.disk_usage()

import shutil

total_b, used_b, free_b = shutil.disk_usage('.')

gib = 2 ** 30 # GiB
gb = 10 ** 9  # GB

print('Total: {:6.2f} GB {:6.2f} GiB'.format(
    total_b / gb, total_b / gib))
print('Used: {:6.2f} GB {:6.2f} GiB'.format(
    used_b/gb, used_b / gib))
print('Free: {:6.2f} GB {:6.2f} GiB'.format(
    free_b / gb, free_b / gib))

'''RESULTS:
Total: 496.76 GB 462.64 GiB
Used:  58.02 GB  54.04 GiB
Free: 413.43 GB 385.04 GiB
'''
