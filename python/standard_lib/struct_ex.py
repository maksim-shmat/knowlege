"""struct about."""

#1 struct pack

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('Original values:', values)
print('Format string:', s.format)
print('Uses:', s.size, 'bytes')
print('Packed Value:', binascii.hexlify(packed_data))

'''RESULTS:
Original values: (1, b'ab', 2.7)
Format string: I 2s f
Uses: 12 bytes
Packed Value: b'0100000061620000cdcc2c40'
'''

#2 struct unpack

import struct
import binascii

packed_dat = binascii.unhexlify(b'0100000061620000cdcc2c40')
s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values:', unpacked_data)

'''RESULTS:
Unpacked Values: (1, b'ab', 2.700000047683716)
'''

#3 struct buffers

import array
import binascii
import ctypes
import struct

s = struct.Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
print('Original:', values)

print()
print('ctypes string buffer')

b = ctypes.create_string_buffer(s.size)
print('Before:', binascii.hexlify(b.raw))
s.pack_into(b, 0, *values)
print('After:', binascii.hexlify(b.raw))
print('Unpacked:', s.unpack_from(b, 0))

print()
print('array')

a = array.array('b', b'\0' * s.size)

print('Before:', binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('After:', binascii.hexlify(a))
print('Unpacked:', s.unpack_from(a, 0))

'''RESULTS:
Original: (1, b'ab', 2.7)

ctypes string buffer
Before: b'000000000000000000000000'
After: b'0100000061620000cdcc2c40'
Unpacked: (1, b'ab', 2.700000047683716)

array
Before: b'000000000000000000000000'
After: b'0100000061620000cdcc2c40'
Unpacked: (1, b'ab', 2.700000047683716)
'''
