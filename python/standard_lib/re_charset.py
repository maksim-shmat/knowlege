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
