"""How about find in other languages, with regular expressions?"""

# in Python3 str object default use Unicode
# in file re_charset.py i.e. (\w+) find as 'French' that as 'Français'

# if need only ASCII use it flag

import re

text = u'Français łzoty Österreich'
pattern = r'\w+'
ascii_pattern = re.compile(pattern, re.ASCII)
unicode_pattern = re.compile(pattern)

print('Text    :', text)
print('Pattern :', pattern)
print('ASCII   :', list(ascii_pattern.findall(text)))
print('Unicode :', list(unicode_pattern.findall(text)))
