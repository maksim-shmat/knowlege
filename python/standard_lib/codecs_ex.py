"""Different codecs about."""

#1 codecs encodings

import unicodedata

from codecs_to_hex import to_hex


text = 'français'
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print('Original:', repr(text))
print('Encoded :', to_hex(encoded, 1), type(encoded))
print('Decoded :', repr(decoded), type(decoded))

'''RESULTS:
Original: 'français'
Encoded : b'66 72 61 6e c3 a7 61 69 73' <class 'bytes'>
Decoded : 'français' <class 'str'>
'''

#2 The second example on the file codecs_open_write.py need testing

#3 The third is the same as the second

#4 secuence order of bytes big-endian(from high to low) and little-endian(fromlow to high)
import codecs
from codecs_to_hex import to_hex

BOM_TYPES = [
        'BOM', 'BOM_BE', 'BOM_LE',
        'BOM_UTF8',
        'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE',
        'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE',
]

for name in BOM_TYPES:
    print('{:12} : {}'.format(
        name, to_hex(getattr(codecs, name), 2)))

'''RESULTS:
BOM          : b'fffe'
BOM_BE       : b'feff'
BOM_LE       : b'fffe'
BOM_UTF8     : b'efbb bf'
BOM_UTF16    : b'fffe'
BOM_UTF16_BE : b'feff'
BOM_UTF16_LE : b'fffe'
BOM_UTF32    : b'fffe 0000'
BOM_UTF32_BE : b'0000 feff'
BOM_UTF32_LE : b'fffe 0000'
'''

#5 create special define

import codecs
from codecs_to_hex import to_hex

if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'

print('Native order    :', to_hex(codecs.BOM_UTF16, 2))
print('Selected order  :', to_hex(bom, 2))

encoded_text = 'français'.encode(encoding)
print('{:14}: {}'.format(encoding, to_hex(encoded_text, 2)))

with open('nonnative-encoded.txt', mode='wb') as f:
    f.write(bom)
    f.write(encoded_text)

'''RESULTS:
Native order    : b'fffe'
Selected order  : b'feff'
utf_16_be     : b'0066 0072 0061 006e 00e7 0061 0069 0073'
'''

#6 detection

import codecs
from codecs_to_hex import to_hex

print()
# write raw data
with open('nonnative-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print('Raw    :', to_hex(raw_bytes, 2))

with codecs.open('nonnative-encoded.txt',
                 mode='r',
                 encoding='utf-16',
                 ) as f:
    decoded_text = f.read()

print('Decoded:', repr(decoded_text))

'''RESULTS:
Raw    : b'feff 0066 0072 0061 006e 00e7 0061 0069 0073'
Decoded: 'français'
'''

#7
