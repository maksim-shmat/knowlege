"""base64 ecnoding about."""

#1 base64 b64encode

import base64
import textwrap

'''
# Load it file and cute header
with open(__file__, 'r', encoding='utf-8') as input:
    raw = input.read()
    initial_data = raw.split('#end_pymotw_header')[1]

byte_string = initial_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)

num_initial = len(byte_string)

# Never not be more 2 adding bytes
padding = 3 - (num_initial % 3)

print('{} bytes before encoding'.format(num_initial))
print('Expect {} padding bytes'.format(padding))
print('{} bytes after encoding\n'.format(len(encoding_data)))
print(encoded_data)
'''

#2 base64 b64decode

import base64

'''
encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
decoded_data = base64.b64decode(encoded_data)
print('Encoded :', encoded_data)
print('Decoded :', decoded_data)

RESULTS:
Encoded : b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
Decoded : b'This is the data, in the clear.'
'''

#3 base64 urlsafe

import base64

'''
encodes_with_pluses = b'\xfb\xef'
encodes_with_slashes = b'\xff\xff'

for original in [encodes_with_pluses, encodes_with_slashes]:
    print('Original         :', repr(original))
    print('Standard ecnoding:',
            base64.standard_b64encode(original))
    print('URL-safe encoding:',
            base64.urlsafe_b64encode(original))
    print()

RESULTS:
Original         : b'\xfb\xef'
Standard ecnoding: b'++8='
URL-safe encoding: b'--8='

Original         : b'\xff\xff'
Standard ecnoding: b'//8='
URL-safe encoding: b'__8='
'''

#4 base64 base32

import base64

'''
original_data = b'This is the data, in the clear.'
print('Original:', original_data)

encoded_data = base64.b32encode(original_data)
print('Encoded :', encoded_data)
decoded_data = base64.b32decode(encoded_data)
print('Decoded :', decoded_data)

RESULTS:
Original: b'This is the data, in the clear.'
Encoded : b'KRUGS4ZANFZSA5DIMUQGIYLUMEWCA2LOEB2GQZJAMNWGKYLSFY======'
Decoded : b'This is the data, in the clear.'
'''

#5 base64 base16

import base64

'''
original_data = b'This is the data, in the clear.'
print('Original:', original_data)

encoded_data = base64.b16encode(original_data)
print('Encoded :', encoded_data)

decoded_data = base64.b16decode(encoded_data)
print('Decoded :', decoded_data)

RESULTS:
Original: b'This is the data, in the clear.'
Encoded : b'546869732069732074686520646174612C20696E2074686520636C6561722E'
Decoded : b'This is the data, in the clear.'
'''

#6 base64 base85

import base64

'''
original_data = b'This is the data, in the clear.'
print('Original : {} bytes {!r}'.format(
    len(original_data), original_data))

b64_data = base64.b64encode(original_data)
print('b64 Encoded : {} bytes {!r}'.format(
    len(b64_data), b64_data))

b85_data = base64.b85encode(original_data)
print('b85 Encoded : {} bytes {!r}'.format(
    len(b85_data), b85_data))

a85_data = base64.a85encode(original_data)
print('a85 Encoded : {} bytes {!r}'.format(
    len(a85_data), a85_data))

RESULTS:
Original : 31 bytes b'This is the data, in the clear.'
b64 Encoded : 44 bytes b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
b85 Encoded : 39 bytes b'RA^~)AZc?TbZBKDWMOn+EFfuaAarPDAY*K0VR9}'
a85 Encoded : 39 bytes b'<+oue+DGm>FD,5.A79Rg/0JYE+EV:.+Cf5!@<*t'
'''
