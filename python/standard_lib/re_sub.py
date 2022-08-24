"""Substitution from text with regex."""

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text:', text)
print('Bold:', bold.sub(r'<b>\1</b>', text))

#2 sub() for named group

import re

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text:', text)
print('Bold:', bold.sub(r'<b>\g<bold_text></b>', text))

#3 sub() for named group with count

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text:', text)
print('Bold:', bold.sub(r'<b>\1</b>', text, count=1))

#4 subn(), analog sub(), but with counter by default

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text:', text)
print('Bold:', bold.subn(r'<b>\1</b>', text))

#5
