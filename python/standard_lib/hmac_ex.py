"""hmac about. Digital singing. Safe - ???"""

#1 sha

import hmac
import hashlib
'''
digest_maker = hmac.new(
        b'secret-shared-key-goes-here',
        b'',
        hashlib.sha1,
)

with open('hmac_sha.py', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
'''

#2 base64

import base64
import hmac
import hashlib

'''
with open('lorem.txt', 'rb') as f:
    body = f.read()

hash = hmac.new(
        b'secret-shared-key-goes-here',
        body,
        hashlib.sha1,
)

digest = hash.digest()
print(base64.encodestring(digest))
'''

#3 hmac pickle

import hashlib
import hmac
import io
import pickle
import pprint


def make_digest(message):
    '''Return digest of message.'''
    hash = hmac.new(
            b'secret-shared-key-goes-here',
            message,
            hashlib.sha1,
    )
    return hash.hexdigest().encode('utf-8')


class SimpleObject:
    '''Check digest before deserialisation.'''
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
out_s = io.BytesIO() 
# write correct object to thread digest/nlength/npickle

o = SimpleObject('digest matches')
pickled_data = pickle.dumps(o)
digest = make_digest(b'not the pickled data at all')
header = b'%s %d\n' % (digest, len(pickled_data))
print('WRITING: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

# write second object with uncorrect digest in thread

o = SimpleObject('digest does not match')
pickled_data = pickle.dumps(o)
digest = make_digest(b'not the pickled data at all')
header = b'%s %d\n' % (digest, len(pickled_data))
print('\nWRITING: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

out_s.flush()

# read socet/thread immitation

in_s = io.BytesIO(out_s.getvalue())

# Read data
while True:
    first_line = in_s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(b' ')
    incoming_length = int(incoming_length.decode('utf-8'))
    print('\nREAD:', incoming_digest, incoming_length)

incoming_pickled_data = in_s.read(incoming_length)

actual_digest = make_digest(incoming_pickled_data)
print('ACTUAL:', actual_digest)

if hmac.compare_digest(actual_digest, incoming_digest):
    obj = pickle.loads(incoming_pickled_data)
    print('OK:', obj)
else:
    print('WARNING: Data corruption')
