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

#
