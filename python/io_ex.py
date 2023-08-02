"""IO input/output about."""

#1 string io

import io


stream = io.StringIO()
stream.write('How many chances?\n')
print('Beacause you lucky, all chances with you!', file=stream)

contents = stream.getvalue()
print(contents)

stream.close()

#2 string io with more elegant

with io.StringIO() as stream:
    stream.write('Learning Python Programming.\n')
    print('Become a Python ninja!', file=stream)
    contents = stream.getvalue()
    print(contents)


How many chances?
Beacause you lucky, all chances with you!

Learning Python Programming.
Become a Python ninja!

