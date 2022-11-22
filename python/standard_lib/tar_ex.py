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
