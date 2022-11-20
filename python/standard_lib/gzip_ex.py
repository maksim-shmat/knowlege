"""GNU zip about."""

#1 write

import gzip
import io
import os

outfilename = 'example.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('Contents of the example file go here.\n')

print(outfilename, 'contains', os.stat(outfilename).st_size,
        'bytes')
os.system('file -b --mime {}'.format(outfilename))

'''RESULTS:
example.txt.gz contains 78 bytes
application/gzip; charset=binary
'''

#2 compress level

import gzip
import io
import os
import hashlib


def get_hash(data):
    return hashlib.md5(data).hexdigest()

data = open('lorem.txt', 'r').read() * 1024

cksum = get_hash(data.encode('utf-8'))

print('Level  Size        Checksum')
print('-----  ----------  -----------------------------------')
print('data   {:>10}  {}'.format(len(data), cksum))

for i in range(0, 10):
    filename = 'compress-level-{}.gz'.format(i)
    with gzip.open(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
        size = os.stat(filename).st_size
        cksum = get_hash(open(filename, 'rb').read())
        print('{:>5d}  {:>10d}  {}'.format(i, size, cksum))

'''RESULTS:
Level  Size        Checksum
-----  ----------  -----------------------------------
data       756736  5bea5d53e093ebb00454c2c5a4325e3f
    0      756846  e390a8360dc4ef0df4f3ceba2e0d9f5e
    1        9056  1c302a92205a3403c5939726194a9cf8
    2        8129  b74c42dcfd8c7068592da714b15735dd
    3        9070  bad91d39bc95bea23cb46b3cce43c980
    4        4177  556749fd33b85a0001a104ffe347d488
    5        4177  969d66c94288402975ba9bf1589f7151
    6        4177  ad14ebb7b0c5686d27d901da3af24c81
    7        4177  cef08d6c50f3efbccd96fc0aa064ea5c
    8        4177  4e4341c7da10539e215573ca9cedf4eb
    9        4177  645e7ac0e5d7e8dc9b4e32eb97b79c34
'''

#3 gzip writelines

import gzip
import io
import itertools
import os


with gzip.open('example_lines.txt.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(
                itertools.repeat('The same line, over and over.\n', 10)
        )

os.system('gzcat example_lines.txt.gz')

'''RESULTS:
sh: 1: gzcat: not found
'''

#4 gzip read

import gzip
import io

with gzip.open('example.txt.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())

'''RESULTS:
Contents of the example file go here.
'''

#5 gzup seek

import gzip


with gzip.open('example.txt.gz', 'rb') as input_file:
    print('Entire file:')
    all_data = input_file.read()
    print(all_data)
    expected = all_data[5:15]

    # go to start
    input_file.seek(0)

    # go on to 5 bite
    input_file.seek(5)
    print('Starting at position 5 for 10 bytes:')
    partial = input_file.read(10)
    print(partial)

    print()
    print(expected == partial)

'''RESULTS:
Entire file:
b'Contents of the example file go here.\n'
Starting at position 5 for 10 bytes:
b'nts of the'

True
'''

#6 gzip BytsIO
