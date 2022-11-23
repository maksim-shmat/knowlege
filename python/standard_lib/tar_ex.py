"""tar archives about."""

#1 tarfile is tarfile

import tarfile

for filename in ['README.txt', 'example.tar',
                 'bad_example.tar', 'notthere.tar']:
    try:
        print('{:>15}  {}'.format(filename, tarfile.is_tarfile(
            filename)))
    except IOError as err:
        print('{:>15}  {}'.format(filename, err))

'''RESULTS:
README.txt  False
    example.tar  False
bad_example.tar  [Errno 2] No such file or directory: 'bad_example.tar'
   notthere.tar  [Errno 2] No such file or directory: 'notthere.tar'
'''

#2 tarfile getnames

import tarfile
'''
with tarfile.open('example.tar', 'r') as t:
    print(t.getnames())

EXPECTED RESULTS:
['index.rst', 'README.txt']
'''

#3 tarfile getmembers

import tarfile
import time
'''
with tarfile.open('example.tar', 'r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print('  Modified:', time.ctime(member_info.mtime))
        print('  Mode    :', oct(member_info.mode))
        print('  Type    :', member_info.type)
        print('  Size    :', member_info.size, 'bytes')
        print()

EXPECTED RESULTS:
index.rst
  Modified: Fri Aug 22 16:22:40 2020
    Mode : 0o644
    Type : b'0'
    Size : 9878 bytes

README.txt
  Modified: Sun Sep 10 11:24:47 2011
    Mode : 0o644
    Type : b'0'
    Size : 23 bytes
'''

#4 tarfile getmember

import tarfile
import time

'''
with tarfile.open('example.tar', 'r') as t:
    for filename in ['README.txt', 'nothere.txt']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print('ERROR: Did not find {} in tar archive'.format(filename))
        else:
            print('{} is {:d} bytes'.format(
                info.name, info.size))

EXPECTED RESULTS:
README.txt is 45 bytes
ERROR: Did not find notthere.txt in tar archive
'''

#5 tarfile extractfile

import tarfile

'''
with tarfile.open('example.tar', 'r') as t:
    for filename in ['README.txt', 'notthere.txt']:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print('ERROR: Did not find {} in tar archive'.format(
                filename))
        else:
            print(filename, ':')
            print(f.read().decode('utf-8'))

EXPECTED RESULTS:
RESDME.txt :
    The examples for the tarfile module use this file and
    example.tar as data.
ERROR: Did not find notthere.txt in tar archive
'''

#6 tarfile extract

import tarfile
import os

'''
os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extract('README.txt', 'outdir')
print(os.listdir('outdir'))

EXPECTED RESULTS:
    ['README.txt']
'''

#7 tarfile extractall

import tarfile
import os

'''
os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extractall('outdir')
print(os.listdir('outdir'))

EXPECTED RESULTS:
    ['README.txt', 'index.rst']
'''

#8 tarfile extractall members

import tarfile
import os

'''
os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extractall('outdir',
                 members=[t.getmember('README.txt')],
                 )
print(os.listdir('outdir'))

EXPECTED RESULTS:
    ['README.txt']
'''

#9 tarfile add

import tarfile

print('creating archive')
with tarfile.open('tarfile_add.tar', mode='w') as out:
    print('adding README.txt')
    out.add('README.txt')

print()
print('Contents:')
with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)

'''RESULTS:
creating archive
adding README.txt

Contents:
README.txt
'''

#10 Other name for TarInfo obj with addfile()

import tarfile

print('creating archive')
with tarfile.open('tarfile_addfile.tar', mode='w') as out:
    print('adding README.txt as RENAMED.txt')
    info = out.gettarinfo('README.txt', arcname='RENAMED.txt')
    out.addfile(info)

print()
print('Contents:')
with tarfile.open('tarfile_addfile.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)

'''RESULTS:
Contents:
README.txt
creating archive
adding README.txt as RENAMED.txt

Contents:
RENAMED.txt
'''

#11 tarfile addfile() from memory

import io
import tarfile

text = 'This is the data to write to the archive.'
data = text.encode('utf-8')

with tarfile.open('addfile_string.tar', mode='w') as out:
    info = tarfile.TarInfo('made_up_file.txt')
    info.size = len(data)
    out.addfile(info, io.BytesIO(data))

print('Contents:')
with tarfile.open('addfile_string.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        f = t.extractfile(member_info)
        print(f.read().decode('utf-8'))

'''RESULTS:
Contents:
made_up_file.txt
This is the data to write to the archive.
'''

#12 tarfile append file to exist archive

import tarfile

print('creating archive')
with tarfile.open('tarfile_append.tar', mode='w') as out:
    out.add('README.txt')

print('contents:',)
with tarfile.open('tarfile_append.tar', mode='r') as t:
    print([m.name for m in t.getmembers()])

print('adding index.rst')
with tarfile.open('tarfile_append.tar', mode='a') as out:
    out.add('index.rst')

print('contents:',)
with tarfile.open('tarfile_append.tar', mode='r') as t:
    print([m.name for m in t.getmembers()])

'''RESULTS:
creating archive
contents:
['README.txt']
adding index.rst
contents:
['README.txt', 'index.rst']
'''

#13 tarfile work whith gzip/bzip2 compressed files 

import tarfile
import os

fmt = '{:<30} {:<10}'
print(fmt.format('FILENAME', 'SIZE'))
print(fmt.format('README.txt', os.stat('README.txt').st_size))

FILES = [
        ('tarfile_compression.tar', 'w'),
        ('tarfile_compression.tar.gz', 'w:gz'),
        ('tarfile_compression.tar.bz2', 'w:bz2'),
]

for filename, write_mode in FILES:
    with tarfile.open(filename, mode=write_mode) as out:
        out.add('README.txt')

    print(fmt.format(filename, os.stat(filename).st_size),
            end=' ')
    print([
        m.name
        for m in tarfile.open(filename, 'r:*').getmembers()
    ])

'''RESULTS:
FILENAME                       SIZE      
README.txt                     0         
tarfile_compression.tar        10240      ['README.txt']
tarfile_compression.tar.gz     210        ['README.txt']
tarfile_compression.tar.bz2    189        ['README.txt']
'''
