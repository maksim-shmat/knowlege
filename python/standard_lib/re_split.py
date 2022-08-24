"""Splitting text with regex for pattern."""

import re

text = """Paragraph one
on tow lines.

Paragraph two.

Paragraph three."""

for num, para in enumerate(re.findall(r'(.+?)\n{2,}',
                                      text,
                                      flags= re.DOTALL)
                           ):
    print(num, repr(para))
    print()

#2 change re.findall() to re.split() 

import re

text = """Paragraph one
on two lines.

Paragraph two.


Paragraph three."""

print('With findall:')
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                       text,
                                       flags=re.DOTALL)):
    print(num, repr(para))
    print()

print()
print('With split:')
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))
print()

#3 split() how str.partition()

import re

text = """Paragraph one
on two lines.

Paragraph two.

Paragraph three."""

print('With split:')
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(para))
    print()

#4
