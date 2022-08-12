"""Base for other examples."""

import re

def test_patterns(text, patterns):
    """Get base text and list of patterns as args, find each pattern
    and show results in stdout."""
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print(" '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',
            [('ab', "'a' followed by 'b'"),
                ])

