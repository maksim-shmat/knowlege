"""zlib about."""

#1 zlib memory

import zlib
import binascii

original_data = b'This is the original text.'
print('Original    :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed  :', len(compressed),
        binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed:', len(decompressed), decompressed)

'''RESULTS:
Original    : 26 b'This is the original text.'
Compressed  : 32 b'789c0bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a123d007f2f097e'
Decompressed: 26 b'This is the original text.'
'''

#2 zlib lengths for example

import zlib

original_data1 = b'This is the original text.'

template = '{:>15} {:>15}'
print(template.format('len(data)', 'len(compressed)'))
print(template.format('-' * 15, '-' * 15))

for i in range(5):
    data = original_data * i
    compressed = zlib.compress(data)
    highlight = '*' if len(data) < len(compressed) else ''
    print(template.format(len(data), len(compressed)), highlight)

'''RERULTS:
      len(data) len(compressed)
--------------- ---------------
              0               8 *
             26              32 *
             52              35 
             78              35 
            104              36 
'''

#3 zlib compresslevel

import zlib

input_data = b'Some repeated text.\n' * 1024
template = '{:>5} {:>5}'

print(template.format('Level', 'Size'))
print(template.format('-----', '----'))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))

'''RESULTS:
Level  Size
-----  ----
    0 20491
    1   172
    2   172
    3   172
    4    98
    5    98
    6    98
    7    98
    8    98
    9    98
'''

#4 zlib incremental, if momory low put data to compress()

import zlib
import binascii

compressor = zlib.compressobj(1)

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

#5 zlib mixed compressed data with free data for decompressobj()

import zlib

lorem = open('lorem.txt', 'rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('Decompressed matches lorem:', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem :', unused_matches)

'''RESULTS:
Decompressed matches lorem: True
Unused data matches lorem : True
'''

#6 
