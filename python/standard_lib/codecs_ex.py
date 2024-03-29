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

#7 rot13

import codecs
import io

buffer = io.StringIO()
stream = codecs.getwriter('rot_13')(buffer)

text = 'abcdefghijklmnopqrstuvwxyz'

stream.write(text)
stream.flush()

print('Original:', text)
print('ROT-13:', buffer.getvalue())

'''RESULTS:
Original: abcdefghijklmnopqrstuvwxyz
ROT-13: nopqrstuvwxyzabcdefghijklm
'''

#8 zlib

import codecs
import io

from codecs_to_hex import to_hex

buffer = io.BytesIO()
stream = codecs.getwriter('zlib')(buffer)

text = b'abcdefghijklmnopqrstuvwxyz\n' * 50

stream.write(text)
stream.flush()

print('Original length:', len(text))
compressed_data = buffer.getvalue()
print('ZIP compressed:', len(compressed_data))

buffer = io.BytesIO(compressed_data)
stream = codecs.getreader('zlib')(buffer)

first_line = stream.readline()
print('Read first line:', repr(first_line))

uncompressed_data = first_line + stream.read()
print('Uncompressed:', len(uncompressed_data))
print('Same:', text == uncompressed_data)

'''RESULTS:
Original length: 1350
ZIP compressed: 48
Read first line: b'abcdefghijklmnopqrstuvwxyz\n'
Uncompressed: 1350
Same: True
'''

#9 incremental coding, bz2

import codecs
import sys

from codecs_to_hex import to_hex

text = b'abcdefjhijklmnopqrstuvwxyz\n'
repetitions = 50

print('Text length :', len(text))
print('Repetitions :', repetitions)
print('Expected len:', len(text) * repetitions)

# Make a bulk of data
encoder = codecs.getincrementalencoder('bz2')()
encoded = []

print()
print('Encoding:', end=' ')
last = repetitions - 1
for i in range(repetitions):
    en_c = encoder.encode(text, final=(i == last))
    if en_c:
        print('\nEncoded: {} bytes'.format(len(en_c)))
        encoded.append(en_c)
    else:
        sys.stdout.write('.')

all_encoded = b''.join(encoded)
print()
print('Total encoded length:', len(all_encoded))
print()

# Decode byte string for one byte
decoder = codecs.getincrementaldecoder('bz2')()
decoded = []

print('Decoding:', end=' ')
for i, b in enumerate(all_encoded):
    final = (i + 1) == len(text)
    c = decoder.decode(bytes([b]), final)
    if c:
        print('\nDecoded : {} characters'.format(len(c)))
        print('Decoding:', end=' ')
        decoded.append(c)
    else:
        sys.stdout.write('.')
print()

restored = b''.join(decoded)

print()
print('Total uncompressed length:', len(restored))

'''RESULTS:
Text length : 27
Repetitions : 50
Expected len: 1350

Encoding: .................................................
Encoded: 98 bytes

Total encoded length: 98

Decoding: .......................................................................................
Decoded : 1350 characters
Decoding: ..........

Total uncompressed length: 1350
'''

#10  invertcaps (don't effective example)

import string

def invertcaps(text):
    """Return new string with new form of caps."""
    return ''.join(
            c.upper() if c in string.ascii_lowercase
            else c.lower() if c in string.ascii_uppercase
            else c
            for c in text
    )

if __name__ == '__main__':
    print(invertcaps('ABCdef'))
    print(invertcaps('abcDEF'))

'''RESULTS:
abcDEF
ABCdef
'''

#11 invertcaps charmap

import codecs
import string

decoding_map = codecs.make_identity_dict(range(256))

pairs = list(zip(
    [ord(c) for c in string.ascii_lowercase],
    [ord(c) for c in string.ascii_uppercase],
))

decoding_map.update({
    upper: lower
    for (lower, upper)
    in pairs
})

decoding_map.update({
    lower: upper
    for (lower, upper)
    in pairs
})

encoding_map = codecs.make_encoding_map(decoding_map)

if __name__ == '__main__':
    print(codecs.charmap_encode('abcDEF', 'strict',
                                encoding_map))
    print(codecs.charmap_decode(b'abcDEF', 'strict',
                                decoding_map))
    print(encoding_map == decoding_map)

'''RESULTS:
(b'ABCdef', 6)
('ABCdef', 6)
True
'''

#12 codecs_invertcaps error
'''
import codecs
from codecs_invertcaps_charmap import encoding_map  # example above

text = 'pi: \u03c0'

for error in ['ignore', 'replace', 'strict']:
    try:
        encoded = codecs.charmap_encode(
                text, error, encoding_map)
    except UnicodeEncodeError as err:
        encoded = str(err)
    print('{:7}: {}'.format(error, encoded))

EXPECTED RESULTS:
ignore : (b'PI: ', 5)
replace: (b'PI: ?', 5)
strict : 'charmap' codec can`t encode character '\u03c0' in
position r: character maps to <undefined>
'''

#13 codecs register and search codec

import codecs
import encodings

def search1(encoding):
    print('search1: Search for:', encoding)
    return None

def search2(encoding):
    print('search2: Searching for:', encoding)
    return None

codecs.register(search1)
codecs.register(search2)

utf8 = codecs.lookup('utf-8')
print('UTF-8:', utf8)

try:
    unknown = codecs.lookup('no-such-encoding')
except LookupError as err:
    print('ERROR:', err)

'''RESULTS:
UTF-8: <codecs.CodecInfo object for encoding utf-8 at 0x7fdd786d97e0>
search1: Search for: no_such_encoding
search2: Searching for: no_such_encoding
ERROR: unknown encoding: no-such-encoding
'''

#14 invertcaps CodecInfo

import codecs

from codecs_invertcaps_charmap import encoding_map, decoding_map


class InvertCapsCodec(codecs.Codec):
    """Coder/decoder without save it."""

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)


class InvertCapsIncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        data, nbytes = codecs.charmap_encode(input,
                                             self.errors,
                                             encoding_map)
        return data


class InvertCapsIncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        data, nbytes = codecs.charmap_decode(input,
                                             self.errors,
                                             decoding_map)
        return data


class InvertCapsStreamReader(InvertCapsCodec, codecs.StreamReader):

    pass


class InvertCapsStreamWriter(InvertCapsCodec, codecs.StreamWriter):

    pass

def find_invertcaps(encoding):
    """Return codec for 'invertcaps'."""
    if encoding == 'invertcaps':
        return codecs.CodecInfo(
                name='invertcaps',
                encode=InvertCapsCodec().encode,
                decode=InvertCapsCodec().decode,
                incrementalencoder=InvertCapsIncrementalEncoder,
                incrementaldecoder=InvertCapsIncrementalDecoder,
                streamreader=InvertCapsStreamReader,
                streamwriter=InvertCapsStreamWriter,
        )
    return None

codecs.register(find_invertcaps)

if __name__ == '__main__':

    # Encoder/Decoder without save it
    encoder = codecs.getencoder('invertcaps')
    text = 'abcDEF'
    encoded_text, consumed = encoder(text)
    print('Encoded "{}" to "{}", consuming {} characters'.format(
        text, encoded_text, consumed))

    # stream write object
    import io
    buffer = io.BytesIO()
    writer = codecs.getwriter('invertcaps')(buffer)
    print('StreamWriter for io buffer: ')
    print(' writing "abcDEF"')
    writer.write('abcDEF')
    print('  buffer contents: ', buffer.getvalue())

    # Incremental decoder
    decoder_factory = codecs.getincrementaldecoder('invertcaps')
    decoder = decoder_factory()
    decoded_text_parts = []
    for c in encoded_text:
        decoded_text_parts.append(
                decoder.decode(bytes([c]), final=False)
        )
    decoded_text_parts.append(decoder.decode(b'', final=True))
    decoded_text = ''.join(decoded_text_parts)
    print('IncrementalDecoder converte {!r} to {!r}'.format(
        encoded_text, decoded_text))

'''RESULTS:
Encoded "abcDEF" to "b'ABCdef'", consuming 6 characters
StreamWriter for io buffer: 
 writing "abcDEF"
  buffer contents:  b'ABCdef'
IncrementalDecoder converte b'ABCdef' to 'abcDEF'
'''
