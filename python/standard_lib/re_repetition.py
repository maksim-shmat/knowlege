"""Find pattern 'n' ones."""

from re_test_patterns import test_patterns

test_patterns(
        'abbaabbba',
        [('ab*', 'a followed by zero or more b'),
         ('ab+', 'a followed by one or more b'),
         ('ab?', 'a followed be zero or one b'),
         ('ab{3}', 'a followed by three b'),
         ('ab{2,3}', 'a follwed by two to three b')],
)

# stdout without 'b', add <?> for it.

test_patterns(
        'abbaabbba',
        [('ab*?', 'a -> by zero or more b'),
         ('ab+?', 'a -> by zero or more b'),
         ('ab??', 'a -> by zero or more b'),
         ('ab{3}?', 'a -> by three b'),
         ('ab{2,3}?', 'a -> by two to three b')],
)
