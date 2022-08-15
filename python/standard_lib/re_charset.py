"""Find set of characters."""

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

# 
