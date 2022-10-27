"""Run this file with: codex_open_write.py utf-8
                                           utf-16
                                           utf-32
"""

import codecs
import sys

from codecs_to_hex import to_hex


encoding = sys.argv[1]
filename = encoding + '.txt'

print('Writing to', filename)
with codecs.open(filename, mode='w', encoding=encoding) as f:
    f.write('français')

    # definition for group of bytes with to_hex()
    nbytes = {
            'utf-8': 1,
            'utf-16': 2,
            'utf-32': 4,
    }.get(encoding, 1)

    # show row bytes on the file
    print('File contents:')
    with open(filename, mode='rb') as f:
        print(to_hex(f.read(), nbytes))

'''EXPECTED RESULTS:
$ python3 codecs_open_write.py utf-8
Writing to utf-8.txt
File contents:
b'66 72 61 6e сЗ a7 61 69 73’
$ python3 codecs_open_write.py utf-16
Writing to utf-16.txt
File contents:
b'fffe 6600 7200 6100 6e00 e700 6100 6900 7300'
$ python3 codecs_open_write.py utf-32
Writing to utf-32.txt
File contents:
b'fffe0000 66000000 72000000 61000000 6e000000 e7000000 61000000
69000000 73000000'
'''

#2 codecs open read

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Reading from', filename)
with codecs.open(filename, mode='r', encoding=encoding) as f:
    print(repr(f.read()))

# from results of previous program
'''EXPECTED RESULTS:
$ python3 codecs_open_read.py utf-8
Reading from utf-8.txt
'frangais’
$ python3 codecs_open_read.py utf-16
Reading from utf-16.txt
'frangais’
$ python3 codecs_open_read.py utf-32
Reading from utf-32.txt
’franqais’
'''
