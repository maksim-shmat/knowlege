"""os.path about."""

#1 os.path.split()

import os.path

PATHS = [
        '/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

'''RESULTS:
 '/one/two/three' : ('/one/two', 'three')
'/one/two/three/' : ('/one/two/three', '')
              '/' : ('/', '')
              '.' : ('', '.')
               '' : ('', '')
'''

#2
