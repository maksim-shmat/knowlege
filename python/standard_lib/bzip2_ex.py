"""bz2 compressed about."""

#1 bz2 work with all data from memory

import bz2
import binascii

original_data = b'This is the original text.'
print('Original    : {} bytes'.format(len(original_data)))
print(original_data)

print()
compressed = bz2.compress(original_data)
print('Compressed  : {} bytes'.format(len(compressed)))
hex_version = binascii.hexlify(compressed)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i * 40:(i + 1) * 40])

print()
decompressed = bz2.decompress(compressed)
print('Decompressed : {} bytes'.format(len(decompressed)))
print(decompressed)

'''RESULTS:
Original    : 26 bytes
b'This is the original text.'

Compressed  : 62 bytes
b'425a683931415926535916be35a6000002938040'
b'01040022e59c402000314c000111e93d434da223'
b'028cf9e73148cae0a0d6ed7f17724538509016be'
b'35a6'

Decompressed : 26 bytes
b'This is the original text.'
'''

#2 bz2 lengths

import bz2

original_data = b'This is the original text.'

fmt = '{:>15}  {:>15}'
print(fmt.format('len(data)', 'len(compressed)'))
print(fmt.format('-' * 15, '-' * 15))

for i in range(5):
    data = original_data * i
    compressed = bz2.compress(data)
    print(fmt.format(len(data), len(compressed)), end='')
    print('*' if len(data) < len(compressed) else '')

'''RESULTS:
        len(data)  len(compressed)
---------------  ---------------
              0               14*
             26               62*
             52               68*
             78               70
            104               72

'''

#3 bz2 incremental

import bz2
import binascii
import io

compressor = bz2.BZ2Compressor()

with open('lorem.txt', 'rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressed: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Flushed: {}'.format(binascii.hexlify(remaining)))

'''RESULTS:
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
Flushed: b'425a68393141592653593bfc167500004357800010400524074b003ff7ff004001d385060d0a6689e906800001aa9f8d04a6268d1a34646818d31184698000012a790844d3d23540f51ea69a0c37d3ac733bf6659000751bc019a961a82ec2d4fa49828284005cbcb2fd208f69786d5aa8ca7128e1cb309db02b2f75be35a25a95562f99f10e9f77a3b3eba4916b644b4b54fc50cf8ecf69c6aa4abdcff5aa4f1c6930dab73241ea49e68cf980987c97b99c1a46703329de71141319c59237a8170cf78b11a6247b3b4f8fe99ba937e59c17fb0be73c63c6c7a0dee7951728f336d22e88eac69a37ba638da19fbe3872b92ad179688ced3519329a70eb92e08b629408ee4c5266b7f9b73c73b63856dcd3dcc6081cfd1c2f79eb164c19f9198532e0cdb0e559d3b21539b417752268826a5a095d2f3dfcfefa2f6d2fbedf1536dbadc785c99b2424a52e3934accbfa6412dfaaf2705150d3b43eb7cdd925dbb0a469eea19f838b6286254417918221e75799ab5db7f319489b4c599b04ee8983752f2ac9f4106888508e0646bf06dd00b42b9f92c3d0cd38356ba4838d50b2530d1e47d25bc901ec9f8bb9229c28481dfe0b3a80'
'''

#4 bz2 file write

import bz2
import io
import os

data = 'Contents of the example file go here.\n'

with bz2.BZ2File('example.bz2', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write(data)

os.system('file example.bz2')

'''RESULTS:
example.bz2: bzip2 compressed data, block size = 900k
'''

#5 bz2 file compresslevel

import bz2
import io
import os

data = open('lorem.txt', 'r', encoding='utf-8').read() * 1024
print('Input contains {} bytes'.format(
    len(data.encode('utf-8'))))

for i in range(1, 10):
    filename = 'compress-level-{}.bz2'.format(i)
    with bz2.BZ2File(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
    os.system('cksum {}'.format(filename))

'''RESULTS:
Input contains 756736 bytes
330387786 9091 compress-level-1.bz2
3852578221 5024 compress-level-2.bz2
3954830888 3784 compress-level-3.bz2
1505447972 2642 compress-level-4.bz2
3690280528 2634 compress-level-5.bz2
3535072046 2563 compress-level-6.bz2
3140208700 2433 compress-level-7.bz2
3159923130 1130 compress-level-8.bz2
207987451 1130 compress-level-9.bz2
'''

#6 bz2 file writelines

import bz2
import io
import itertools
import os

data = 'The same line, over and over.\n'

with bz2.BZ2File('lines.bz2', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(itertools.repeat(data, 10))

os.system('bzcat lines.bz2')

'''RESULTS:
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
'''

#7 bz2 file read

import bz2
import io

with bz2.BZ2File('example.bz2', 'rb') as input:
    with io.TextIOWrapper(input, encoding='utf-8') as dec:
        print(dec.read())

'''RESULTS:
Contents of the example file go here.
'''

#8 read chunk of file with seek()

import bz2
import contextlib

with bz2.BZ2File('example.bz2', 'rb') as input:
    print('Entire file:')
    all_data = input.read()
    print(all_data)

    expected = all_data[5:15]

    # go to the start
    input.seek(0)

    # go to 5 bytes 
    input.seek(5)
    print('Starting at position 5 for 10 bytes:')
    partial = input.read(10)

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

#9 bz2 unicode, bz2.open() for io.TextIOWrapper for auto encode/decode

import bz2
import os

data = 'Character with an accent.'

with bz2.open('example.bz2', 'wt', encoding='utf-8') as output:
    output.write(data)

with bz2.open('example.bz2', 'rt', encoding='utf-8') as input:
    print('Full file: {}'.format(input.read()))

# go to start simbol with accent
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input:
    input.seek(18)
    print('One character: {}'.format(input.read(1)))

# Go to middle simbol with accent
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input:
    input.seek(19)
    try:
        print(input.read(1))
    except UnicodeDecodeError:
        print('ERROR: failed to decode')

'''RESULTS:
Full file: Character with an accent.
One character: a
c

EXPECTED RESULTS:
    Full file: Character with an ǡccent.
    One character: â
    Error: failed to decode

'''
