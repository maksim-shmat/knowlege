"""atexit about."""

#1 atexit simple

import atexit

'''
def all_done():
    print('all_done()')

print('Registering')
atexit.register(all_done)
print('Registered')

RESULTS:
Registering
Registered
all_done()
'''

#2
