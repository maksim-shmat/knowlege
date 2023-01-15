"""Analize text with shlex."""

#1 shlex example

import shlex
import sys

'''
if len(sys.argv) != 2:
    print('Please specify one filename on the command line.')
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as f:
    body = f.read()
print('ORIGINAL: {!r}'.format(body))
print()

print('TOKENS:')
lexer = shlex.shlex(body)
for token in lexer:
    print('{!r}'.format(token))
'''

#2 shlex quote

import shlex

'''
examples = [
        "Embedded'SingleQuote",
        'Embedded"DoubleQuote',
        'Embedded Space',
        '~SpecialCharacter',
        r'Back\slash',
]

for s in examples:
    print('ORIGINAL : {}'.format(s))
    print('QUOTED   : {}'.format(shlex.quote(s)))
    print()

RESULTS:
ORIGINAL : Embedded'SingleQuote
QUOTED   : 'Embedded'"'"'SingleQuote'

ORIGINAL : Embedded"DoubleQuote
QUOTED   : 'Embedded"DoubleQuote'

ORIGINAL : Embedded Space
QUOTED   : 'Embedded Space'

ORIGINAL : ~SpecialCharacter
QUOTED   : '~SpecialCharacter'

ORIGINAL : Back\slash
QUOTED   : 'Back\slash'
'''

#3 shlex split

import shlex

'''
text = """This text has "quoted parts" inside it."""
print('ORIGINAL: {!r}'.format(text))
print()

print('TOKENS:')
print(shlex.split(text))

RESULTS:
ORIGINAL: 'This text has "quoted parts" inside it.'

TOKENS:
['This', 'text', 'has', 'quoted parts', 'inside', 'it.']
'''

#4 shlex source

import shlex

'''
text = "This text says to source quotes.txt before continuing."
print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print('TOKENS:')
for token in lexer:
    print('{!r}'.format(token))
'''

#5 shlex table

import shlex

'''
text = """|Col 1||Col 2|| Col 3|"""
print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.quotes = '|'

print('TOKENS:')
for token in lexer:
    print('{!r}'.format(token))

RESULTS:
ORIGINAL: '|Col 1||Col 2|| Col 3|'

TOKENS:
'|Col 1|'
'|Col 2|'
'| Col 3|'
'''

#6 shlex whitespace

import shlex
import sys

'''
if len(sys.argv) != 2:
    print('Please specify one filename on the command line.')
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as f:
    body = f.read()
print('ORIGINAL: {!r}'.format(body))
print()

print('TOKENS:')
lexer = shlex.shlex(body)
lexer.whitespace += '.,'
for token in lexer:
    print('{!r}'.format(token))
'''

#7  shlex errors

import shlex

'''
text = """This line is OK.
This line has an "unfinished quote.
This line is OK, too.
"""

print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
print('TOKENS:')
try:
    for token in lexer:
        print('{!r}'.format(token))
except ValueError as err:
    first_line_of_error = lexer.token.splitlines()[0]
    print('ERROR: {} {}'.format(lexer.error_leader(), err))
    print('following {!r}'.format(first_line_of_error))
'''

#8 shlex possix

import shlex

'''
examples = [
        'Do"Not"Separate',
        '"Do"Separate',
        'Escaped \e Character not in quotes',
        'Escaped "\e" Character in double quotes',
        "Escaped '\e' Character in single quotes",
        r"Escaped '\'' \"\'\" single quoter",
        r'Escaped "\"" \'\"\' double quote',
        "\"'Strip extra layer of quotes'\"",
]

for s in examples:
    print('ORIGINAL: {!r}'.format(s))
    print('non-POSIX: ', end='')

    non_posix_lexer = shlex.shlex(s, posix=False)
    try:
        print('{!r}'.format(list(non_posix_lexer)))
    except ValueError as err:
        print('error({})'.format(err))

    print('POSIX    :', end='')
    posix_lexer = shlex.shlex(s, posix=True)
    try:
        print('{!r}'.format(list(posix_lexer)))
    except ValueError as err:
        print('error({})'.format(err))
    print()

RESULTS:
ORIGINAL: 'Do"Not"Separate'
non-POSIX: ['Do"Not"Separate']
POSIX    :['DoNotSeparate']

ORIGINAL: '"Do"Separate'
non-POSIX: ['"Do"', 'Separate']
POSIX    :['DoSeparate']

ORIGINAL: 'Escaped \\e Character not in quotes'
non-POSIX: ['Escaped', '\\', 'e', 'Character', 'not', 'in', 'quotes']
POSIX    :['Escaped', 'e', 'Character', 'not', 'in', 'quotes']

ORIGINAL: 'Escaped "\\e" Character in double quotes'
non-POSIX: ['Escaped', '"\\e"', 'Character', 'in', 'double', 'quotes']
POSIX    :['Escaped', '\\e', 'Character', 'in', 'double', 'quotes']

ORIGINAL: "Escaped '\\e' Character in single quotes"
non-POSIX: ['Escaped', "'\\e'", 'Character', 'in', 'single', 'quotes']
POSIX    :['Escaped', '\\e', 'Character', 'in', 'single', 'quotes']

ORIGINAL: 'Escaped \'\\\'\' \\"\\\'\\" single quoter'
non-POSIX: error(No closing quotation)
POSIX    :['Escaped', '\\ \\"\\"', 'single', 'quoter']

ORIGINAL: 'Escaped "\\"" \\\'\\"\\\' double quote'
non-POSIX: error(No closing quotation)
POSIX    :['Escaped', '"', '\'"\'', 'double', 'quote']

ORIGINAL: '"\'Strip extra layer of quotes\'"'
non-POSIX: ['"\'Strip extra layer of quotes\'"']
POSIX    :["'Strip extra layer of quotes'"]
'''
