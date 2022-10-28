"""Codecs decode error about."""

import codecs
import sys

from codecs_to_hex import to_hex

error_handling = sys.argv[1]

text = 'français'
print('Original    :', repr(text))

# Save data with any codecs
with codecs.open('decode_error.txt', 'w',
                 encoding='utf-16') as f:
    f.write(text)

# Show byted file

with open('decode_error.txt', 'rb') as f:
    print('File contents:', to_hex(f.read(), 1))

# Read data with not right codecs
with codecs.open('decode_error.txt', 'r',
                 encoding='utf-8',
                 errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError as err:
        print('ERROR:', err)
    else:
        print('Read  :', repr(data))

'''RESULTS:
python3 codecs_decode_error.py strict

Original    : 'français'
File contents: b'ff fe 66 00 72 00 61 00 6e 00 e7 00 61 00 69 00 73 00'
ERROR: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

python3 codecs_decode_error.py ignore

Original    : 'français'
File contents: b'ff fe 66 00 72 00 61 00 6e 00 e7 00 61 00 69 00 73 00'
Read        : 'f\x00r\x00a\x00n\x00\x00a\x00i\x00s\x00'

python3 codecs_decode_error.py replace

Original    : 'français'
File contents: b'ff fe 66 00 72 00 61 00 6e 00 e7 00 61 00 69 00 73 00'
Read        : 'f\x00r\x00a\x00n\x00\x00a\x00i\x00s\x00'
'''
