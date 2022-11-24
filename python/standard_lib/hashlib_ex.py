"""hashlib about."""

#1 check algorithms

import hashlib

print('Guaranteed:\n{}\n'.format(
    ', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(
    ', '.join(sorted(hashlib.algorithms_available))))

'''RESULTS:
Guaranteed:
blake2b, blake2s, md5, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256

Available:
blake2b, blake2s, md5, md5-sha1, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, sha512_224, sha512_256, shake_128, shake_256, sm3
'''

#2 hashlib md5

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

'''RESULTS:
cf62fc6ce8178123a2465751c711fa25
'''

#3 sha1

import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

'''RESULTS:
04e991d0a1b5a77a221ce591d216fc0764d15457
'''

#4 new() name of used algorithm

# Call this code from diff file and $ python3 this_file.py sha1
                                                         # sha256
                                                         # sha512
                                                         # md5
'''
import argparse
import hashlib
import sys

from hashlib_data import lorem

parser = argparse.ArgumentParser('hashlib demo')
parser.add_argument(
        'hash_name',
        choices=hashlib.algorithms_available,
        help='the name of the hash algorithm to use',
)
parser.add_argument(
        'data',
        nargs='?',
        default=lorem,
        help='the input data to hash, defaults to lorem ipsum',
)
args = parser.parse_args()

h = hashlib.new(args.hash_name)
h.update(args.data.encode('utf-8'))
print(h.hexdigest())
'''

#5 hashlib increment update

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()


def chunkize(size, text):
    "Return parts of the text in size-based increments."
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return

h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('All at once :', all_at_once)
print('Line by line:', line_by_line)
print('Same        :', (all_at_once == line_by_line))

'''RESULTS:
All at once : cf62fc6ce8178123a2465751c711fa25
Line by line: cf62fc6ce8178123a2465751c711fa25
Same        : True
'''
