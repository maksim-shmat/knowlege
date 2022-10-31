"""EncodeFile() about."""

from codecs_to_hex import to_hex

import codecs
import io


# Raw data
data = 'français'

# handle encoding with UTF-8
utf8 = data.encode('utf-8')
print('Start as UTF-8    :', to_hex(utf8, 1))

# Make a start buffer and wrapped it with class EncodeFile

output = io.BytesIO()
encoded_file = codecs.EncodedFile(output, data_encoding='utf-8',
                                  file_encoding='utf-16')
encoded_file.write(utf8)

# show buffer core

utf16 = output.getvalue()
print('Encoded to UTF-16:', to_hex(utf16, 2))

# Make another buffer for UTF-16 and wrapped it with class EncodeFile

buffer = io.BytesIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8',
                                  file_encoding='utf-16')

# Read data in UTF-8
recoded = encoded_file.read()
print('Back to UTF-8    :', to_hex(recoded, 1))

'''RESULTS:
Start as UTF-8    : b'66 72 61 6e c3 a7 61 69 73'
Encoded to UTF-16: b'fffe 6600 7200 6100 6e00 e700 6100 6900 7300'
Back to UTF-8    : b'66 72 61 6e c3 a7 61 69 73'
'''
