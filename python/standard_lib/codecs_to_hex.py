"""Formating text string. Base file for codecs_ex.py"""

import binascii


def to_hex(t, nbytes):
    """Format text t as units of values with length nbytes,
    with spaces between.
    """
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return b' '.join(
            hex_version[start:start + chars_per_item]
            for start in range(0, len(hex_version), chars_per_item)
    )

if __name__ == '__main__':
    print(to_hex(b'abcdef', 1))
    print(to_hex(b'abcdef', 2))

'''RESULTS:
b'61 62 63 64 65 66'
b'6162 6364 6566'
'''
