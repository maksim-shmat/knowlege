"""TemporaryFile about."""

#1 named temp.file and unnamed Temporary file

import os
import tempfile

print('Building a filename with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('    {!r}'.format(temp))
    print('temp.name:')
    print('    {!r}'.format(temp.name))

# remove temporary file
os.remove(filename)

print()
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('    {!r}'.format(temp))
    print('temp.name:')
    print('    {!r}'.format(temp.name))

'''RESULTS:
Building a filename with PID:
temp:
    <_io.BufferedRandom name='/tmp/guess_my_name.82688.txt'>
temp.name:
    '/tmp/guess_my_name.82688.txt'

TemporaryFile:
temp:
    <_io.BufferedRandom name=3>
temp.name:
    3
'''

#2 binary

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Some data')

    temp.seek(0)
    print(temp.read())

'''RESULSTS:
b'Some data'
'''

#3 text mode

import tempfile

with tempfile.TemporaryFile(mode='w+t') as f:
    f.writelines(['first\n', 'second\n'])

    f.seek(0)
    for line in f:
        print(line.rstrip())

'''RESULTS:
first
second
'''

#3 Named Temporary File

import os
import pathlib
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

    f = pathlib.Path(temp.name)

print('Exists after close:', f.exists())

'''RESULTS:
temp:
  <tempfile._TemporaryFileWrapper object at 0x7f9a5bbeef20>
temp.name:
  '/tmp/tmp02fup_86'
Exists after close: False
'''

#4 Spooled Temporary File

import tempfile

with tempfile.SpooledTemporaryFile(max_size=100,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)

'''RESULTS:
temp: <tempfile.SpooledTemporaryFile object at 0x7efed76aece0>
False <_io.TextIOWrapper encoding='utf-8'>
False <_io.TextIOWrapper encoding='utf-8'>
True <_io.TextIOWrapper name=3 mode='w+t' encoding='utf-8'>
'''

#5 rollover() or fileno() for Spooled Temporary file

import tempfile

print()
with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)
    print('rolling over')
    temp.rollover()
    print(temp._rolled, temp._file)

'''RESULTS:
temp: <tempfile.SpooledTemporaryFile object at 0x7f8899b03a00>
False <_io.TextIOWrapper encoding='utf-8'>
False <_io.TextIOWrapper encoding='utf-8'>
False <_io.TextIOWrapper encoding='utf-8'>
rolling over
True <_io.TextIOWrapper name=3 mode='w+t' encoding='utf-8'>
'''

#6 temporary directory for tempfiles e.g.

import pathlib
import tempfile

print()
with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(the_dir)
    
    a_file = the_dir/'a_file.txt'
    a_file.write_text('This file is deleted.')

print('Directory exists after?', the_dir.exists())
print('Contents after:', list(the_dir.glob('*')))

'''RESULTS:
/tmp/tmp652k229y
Directory exists after? False
Contents after: []
'''

#7 Named Temporary File args

import tempfile

print()
with tempfile.NamedTemporaryFile(suffix='_suffix',
                                prefix='prefix_',
                                dir='/tmp') as tmp:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)

'''RESULTS:
temp:
   <tempfile.SpooledTemporaryFile object at 0x7f87dfa47d60>
temp.name:
   3

but expected another result:
    temp.name:
    /tmp/prefix_q62wd7zl_suffix
'''

#8 
