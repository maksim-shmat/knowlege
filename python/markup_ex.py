"""Simple Markup program."""

# python3 markup_ex.py < jill.txt > jill.html

import sys, re
from util import *  # from file util.py

print('<html><head><title>...</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
    print('</body></html>')
