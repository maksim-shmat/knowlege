"""Regular Expression about."""

# search() + re = match. object

import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))

#2 compile() + re = RegexObject

import re

# First compile regex patterns, for fast fulfilling
regexes = [
        re.compile(p)
        for p in ['this', 'that']
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
            end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')

#3 findall() + re = >1 find object

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))

#4 finditer() + re = iterator -> match. objects

import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(
        text[s:e], s, e))

#5
