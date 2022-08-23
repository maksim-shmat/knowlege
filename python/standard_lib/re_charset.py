"""Find set of characters."""
'''
from re_test_patterns import test_patterns

test_patterns(
        'abbaabbba',
        [('[ab]', 'either a or b'),
         ('a[ab]+', 'a followed by 1 or more a or b'),
         ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)

# charset exclude, add circumflex (^)

test_patterns(
        'This is some text -- with punctuation.',
        [('[^-. ]+', 'sequences without -, ., or space')],
)

# charset ranges

test_patterns(
        'This is some text -- with punctuation.',
        [('[a-z]+', 'sequences of lowercase letters'),
         ('[A-Z]+', 'sequences of uppercase letters'),
         ('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
         ('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
)

# any character in this, add dot (.)

test_patterns(
        'abbaabbba',
        [('a.', 'a followed by any one character'),
         ('b.', 'b followed by any one character'),
         ('a.*b', 'a followed by anything, ending in b'),
         ('a.*?b', 'a followed by anything, ending in b')],
)

# Special sypbols
from  re_test_patterns import test_patterns

test_patterns(
        'A prime #1 example!',
        [(r'\d+', 'sequence of digits'),  # r - row for backward slash
         (r'\D+', 'sequence of non_digits'),
         (r'\s+', 'sequence of whitespace'),
         (r'\S+', 'sequence of non-whitespace'),
         (r'\w+', 'alphanumeric characters'),
         (r'\W+', 'non-alphanumeric')],
)

# for find chunk of regular expression need double slashing
from re_test_patterns import test_patterns

test_patterns(
        r'\d+ \D+ \s+',
        [(r'\\.\+', 'escape code')],
)

# Ancors for find

from re_test_patterns import test_patterns

test_patterns(
        'This is some text -- with punctuation.',
        [(r'^\w+', 'word at start of string'),  # ^ start logical or phis. str
         (r'\A\w+', 'word at start of string'), # $ end of logic. or phis str
         (r'\w+\S*$', 'word near end of string'),  # \A start of logic. str 
         (r'\w+\S*\Z', 'word near end of string'), # \Z end of logical str
         (r'\w*t\w*', 'word containing t'),  # \b empty str in start/end str
         (r'\bt\w+', 't at start of word'),  # \B empty str not in start or end of string
         (r'\w+t\b', 't at end of word'),
         (R'\Bt\B', 't, not start or end of word')],
)

# match() against search() for auto ancor to start string

import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text :', text)
print('Pattern:', pattern)

m = re.match(pattern, text)
print('Match :', m)
s = re.search(pattern, text)
print('Search :', s)

# fullmatch() for whole string == pattern

import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text :', text)
print('Pattern :', pattern)

m = re.search(pattern, text)
print('Search :', m)

s = re.fullmatch(pattern, text)
print('Full match :', s)

# search substring

import re

text = 'This is some text -- with punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')

print('Text:', text)
print()

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print('  {:>2d}  : {:>2d} = "{}"'.format(
        s, e - 1, text[s:e]))
    # go to forward in string 'text' for next search
    pos = e

# groups

from re_test_patterns import test_patterns

test_patterns(
        'abbaaabbbbaaaaa',
        [('a(ab)', 'a followed by literal ab'),
         ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
         ('a(ab)*', 'a followed by 0-n ab'),
         ('a(ab)+', 'a followed by 1-n ab')],
)

# groups with match()

import re

text = 'This is some text -- with punctuation.'

print(text)
print()

patterns = [
        (r'^(\w+)', 'word at start of string'),
        (r'(\w+)\S*$', 'word at end, with optional punctuation'),
        (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
        (r'(\w+t)\b', 'word ending with t'),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print('  ', match.groups())
    print()

# group individual

import re

text = 'This is some text -- with puctuation.'

print('Input text :', text)

# word start with 't' and then nex word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern :', regex.pattern)

match = regex.search(text)
print('Entire match :', match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word :', match.group(2))

# group named

import re

text = 'This is some text -- with punctuation.'
print(text)
print()
patterns = [
        r'^(?P<first_word>\w+)',
        r'(?P<last_word>\w+)\S*$',
        r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
        r'(?P<ends_with_t>\w+t)\b',
]
for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()
    
# test_patterns(), make module re_test_patterns_groups.py from code of beneath

import re

def test_patterns(text, patterns):
    """Get text and list of patterns as arguments, make a search all
    results every pattern in text and return result to stdout.
    """
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print(' {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.start()
            prefix = ' ' * (s)
            print(
                    ' {}{!r}{} '.format(prefix,
                                        text[s:e],
                                        ' ' * (len(text) - e)),
                    end=' ',
            )
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),
                )
        print()
    return

# groups nested

from re_test_patterns_groups import  test_patterns
# make module re_test_patterns_group.py from code upper
test_patterns(
        'abbaabbba',
        [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
)

# re_groups_alternative.py for re_test_patterns_groups.py

from re_test_patterns_groups import test_patterns

# feel the difference with pipe mark (|)
test_patterns(
        'abbaabbba',
        [(r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
         (r'a((a|b)+)', 'a then seq. of [ab]')],
)

# groups noncapturing
from re_test_patterns_groups import test_patterns

test_patterns(
        'abbaabbba',
        [(r'a((a+)|(b_))', 'capturing form'),
         (r'a((?:a+)|(?:b+))', 'noncapturing')],
)

# For compile(), search() match()
# flag IGNORECASE
import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Case-sensitive:')
for match in with_case.findall(text):
    print('  {!r}'.format(match))
print('Case-insensitive:')
for match in without_case.findall(text):
    print('  {!r}'.format(match))

# flag MULTILINE

import re
text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print('Text:\n  {!r}'.format(text))
print('Pattern:\n  {}'.format(pattern))
print('Single Line :')
for match in single_line.findall(text):
    print('  {!r}'.format(match))
print('Multiline    :')
for match in multiline.findall(text):
    print('  {!r}'.format(match))

# flag DOTALL

import re
text = "This is some text -- with punctuation.\nA second line."
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print('Text:\n   {!r}'.format(text))
print('Pattern:\n  {}'.format(pattern))
print('No newlines :')
for match in no_newlines.findall(text):
    print('  {!r}'.format(match))
print('Dotall      :')
for match in dotall.findall(text):
    print('  {!r}'.format(match))


# re compact mode, check correct emails

import re

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

candidates = [
        u'first.last@example.com',
        u'first.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<30} {}'.format(
        candidate, 'Matches' if match else 'No match')
)

# re verbose mode, for check correct emails

import re

address = re.compile(
        """
        [\w\d.+-]+  # Name of user
        @
        ([\w\d.]+\.)+  # Prefix from name of domen
        (com|org|edu)  # TODO: keep other domens of high level
        """,
        re.VERBOSE)

candidates = [
        u'first.last@example.com',
        u'first.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
]
        
for candidate in candidates:
    match = address.search(candidate)
    print('{:<30}  {}'.format(
        candidate, 'Matches' if match else 'No match'),
)

# regular expression with more text, for check correct emails

import re

address = re.compile(
        """

        # Name may contain letters and be include a dot '.'
        # in shortly names
        ((?P<name>
            ([\w.,]+\s+)*[\w.,]+)
            \s*
            # email addresses be into < >, but if name if finded
            # because angle braket be this
            <
        )? # Full name neded

        # email this: username@domain.tld
        (?P<email>
          [\w\d.+-]+  # Name of user
          @
          ([\w\d.]+\.)+  # Prefix from name of domen
          (com|org|edu)  # list of domens how is needed us
        )
        >?  # Closed angle bracket
        """,
        re.VERBOSE)

candidates = [
        u'first.last@example.com',
        u'firts.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
        u'First Last <first.last@example.com>',
        u'No Brackets firts.last@example.com',
        u'First Last',
        u'Firts Middle Last <first.last@example.com>',
        u'<first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')

# flags embeded

import re

text = 'This is some text -- with punctuation.'

pattern = r'(?i)\bT\w+'  # i == IGNORECASE, and more: a == ASCII
                                                    # m == MULTILINE
                                                    # s == DOTALL
                                                    # x == VERBOSE
regex = re.compile(pattern)

print('Text       :', text)
print('Pattern    :', pattern)
print('Matches    :', regex.findall(text))

# look ahead both part of the pattern, positive look

import re

address = re.compile(
        """
        # Name is are letters and dots'.'
        ((?P<name>
        ({\w.,]+\s+)*[\w.,]+
        )
        \s+
    )
    (?= (<.*>$)  # into angle brackets
    |
    ([^<].*[^>]$)  # not into angle brackets
)
<?
(?P<email>
  [\w\d.+-]+
  @
  ([\w\d.]+\.)+
  (com|org|edu)
)
>?
""",
re.VERBOSE)

candidates = [
        u'First Last <first.last@example.com>',
        u'No Brackets first.last@example.com',
        u'Open Bracket <first.last@example.com',
        u'Close Bracket first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')

# negative look in backward for ignore 'noreply' e.g.

import re

address = re.compile(
        """
        ^
        # Address: username@domain.tld
        # Ignore addresses noreply
        (?!noreply@.*$)
        [\w\d.+-]+  # Name of the user
        @
        ([\w\d.]+\.)+  # Prefix domain name
        (com|org|edu)

        $
        """,
        re.VERBOSE)

candidates = [
        u'first.last@example.com',
        u'noreply@example.com',
]
for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('Match:', candidate[match.start():match.end()])
    else:
        print(' No match')

# negative look behind

import re

address = re.compile(
        """
        ^
        # Adress: username@domain.tld
        [\w\d.+-]+  # Name of the user

        # Ignore noreply
        (?<!noreply)

        @
        ([\w\d.]+\.)+
        (com|org|edu)

        $
        """,
        re.VERBOSE)

candidates = [
        u'first.last@example.com',
        u'noreply@example.com',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match:', candidate[match.start():match.end()])
        print()
    else:
        print('No match')

# look behind with (?<=pattern)

import re

twitter = re.compile(
        """
        # user ID from Twitter: @username
        (?<=@)
        ([\w\d_]+)  # username
        """,
        re.VERBOSE)

text = """This text includes two Twitter handles.
One for @ThePSF, and one @kingsman.
"""
print(text)
for match in twitter.findall(text):
    print('Handle:', match)

# backward refer to group

import re

address = re.compile(
        r"""

        # Name
        (\w+)  # First Name
        \s+
        (([\w.]+)\s+)?  # Father's Name
        (\w+)  # Last Name

        \s+

        <

        # Address: firstname.lastname@domain.tld
        (?P<email>
        \1  # firstname
        \.
        \4  # lastname
        @
        ([\w\d.]+\.)+  # domain prefix
        (com|org|edu)  # highlevel domain name
    )
    
    >
    """,
    re.VERBOSE | re.IGNORECASE)

candidates = [
        u'First Last <first.last@example.com>',
        u'Different Name <first.last@example.com>',
        u'First Middle Last <first.last@example.com>',
        u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.group(1), match.group(4))
        print(' Match email:', match.group(5))
    else:
        print(' No match')
print()
# refer to named group with (?P=name)

import re

address = re.compile(
        """

        # FN/LN
        (?P<first_name>\w+)
        \s+
        (([\w.]+)\s+)?  # Father's Name or Initials
        (?P<last_name>\w+)

        \s+

        <

        # Address: fn.ln@domain.tld
        (?P<email>
          (?P=first_name)
          \.
          (?P=last_name)
          @
          ([\w\d.]+\.)+  # Domain name prefix
          (com|org|edu)
        )

        >
        """,
        re.VERBOSE | re.IGNORECASE)

candidates = [
        u'First Last <first.last@example.com>',
        u'Different Name <first.last@example.com>',
        u'First Middle Last <first.last@example.com>',
        u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['first_name'],
                end=' ')
        print(match.groupdict()['last_name'])
        print(' Match email:', match.groupdict()['email'])
    else:
        print(' No match')
print()
'''
# id with (?(id)yes-expression|no-expression)

import re

address = re.compile(
        """
        ^
        
        # Name contain letters and dots
        (?P<name>
          ([\w.]+\s+)*[\w.]+
        )?
        \s*

        # email into angle brackets, but if in the case be name
        (?(name)
          # name contain:
          (?P<brackets>(?=(<.*>$)))
          |
          # name not find
          (?=([^<].*[^>]$))
        )

        # find angle bracket if it both
        (?(brackets)<|\s*)

        # email: username@domain.tld
        (?P<email>
          [\w\d.+-]+  # username
          @
          ([\w\d.]+\.)+  # Domain name prefix
          (com|org|edu)

        # find angle bracket if it both
        (?(brackets)>|\s*)

        $
        """,
        re.VERBOSE)

candidates = [
        u'First Last <first.last@example.com>',
        u'No Brackets first.last@example.com',
        u'Open Bracket <first.last@example.com',
        u'Close Bracket first.last@example.com>',
        u'no.brackets@example.com',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['name'])
        print(' Match email:', match.groupdict()['email'])
    else:
        print(' No match')


