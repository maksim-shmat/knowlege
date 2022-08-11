"""Regular expression examples."""

#1 test pattern
import re

def test_patterns(text, patterns):
    """Get a start text and list of templates how arguments, need find all
    patterns into text and return results to the stdout.
    """
    # find patterns in text and return results
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
                 [('ab', "'a' folowed by 'b'"),
])

