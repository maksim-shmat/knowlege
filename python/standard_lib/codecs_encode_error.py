"""codecs encode error."""



import codecs
import sys

error_handling = sys.argv[1]

text = 'français'

try:
    # save data in ASCII with encode errors mode from CLI
    with codecs.open('encode_error.txt', 'w',
                     encoding='ascii',
                     errors=error_handling) as f:
        f.write(text)
except UnicodeEncodeError as err:
    print('ERROR:', err)
else:
    # in the case how no errors show file example
    with open('encode_error.txt', 'rb') as f:
        print('File contents: {!r}'.format(f.read()))

'''RESULTS: 
# for CLI: python3 codecs_error.py strict

ERROR: 'ascii' codec can't encode character '\xe7' in position 4:
ordinal not in range(128)

# for CLI: python3 codecs_error.py replace

File contents: b'fran?ais'

# for CLI: python3 codecs_error.py ignore

File contents: b'franais'

# for CLI: python3 codecs_error.py xmlcharrefreplace

File contents: b'fran&#231;ais'

# for CLI: python3 codecs_error.py backslashreplace

File contents: b'fran\\xe7ais'
'''
