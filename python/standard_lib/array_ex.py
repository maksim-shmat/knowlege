"""array about."""

#1 array string

import array
import binascii

s = b'This is the array.'
a = array.array('b', s)

print('As byte string:', s)
print('As hex:', binascii.hexlify(a))

'''RESULTS:
As byte string: b'This is the array.'
As hex: b'54686973206973207468652061727261792e'
'''

#2 array sequence

import array
import pprint

a = array.array('i', range(3))
print('Initial:', a)

a.extend(range(3))
print('Extended:', a)

print('Slice:', a[2:5])

print('Iterator:')
print(list(enumerate(a)))

'''RESULTS:
Initial: array('i', [0, 1, 2])
Extended: array('i', [0, 1, 2, 0, 1, 2])
Slice: array('i', [2, 0, 1])
Iterator:
[(0, 0), (1, 1), (2, 2), (3, 0), (4, 1), (5, 2)]
'''

#3 array file

import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)

# write array of integers on the temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)  # need get real file
output.flush()

# read raw data
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read data to array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)

#4 array tobytes()

import array
import binascii

print()
a = array.array('i', range(5))
print('A1:', a)

as_bytes = a.tobytes()
print('Bytes:', binascii.hexlify(as_bytes))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)

#5 arrat byteswap

import array
import binascii

def to_hex(a):
    chars_per_item = a.itemsize * 2  # two 16th integers
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version) // chars_per_item
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]

start = int('0x12345678', 16)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt = '{:>12}  {:>12}  {:>12}  {:>12}'
print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12))
fmt = '{!r:>12}  {:12}  {!r:>12}  {:12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))

'''RESULTS:
      A1 hex            A1        A2 hex            A2
------------  ------------  ------------  ------------
 b'78563412'     305419896   b'12345678'    2018915346
 b'79563412'     305419897   b'12345679'    2035692562
 b'7a563412'     305419898   b'1234567a'    2052469778
 b'7b563412'     305419899   b'1234567b'    2069246994
 b'7c563412'     305419900   b'1234567c'    2086024210
'''
