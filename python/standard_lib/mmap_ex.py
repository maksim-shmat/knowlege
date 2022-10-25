"""mmap module about."""

#1 mmap read

import mmap

with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('First 10 bytes via read :', m.read(10))
        print('First 10 bytes via slice:', m[:10])
        print('2nd   10 bytes via read :', m.read(10))

'''RESULTS:
First 10 bytes via read : b'Lorem ipsu'
First 10 bytes via slice: b'Lorem ipsu'
2nd   10 bytes via read : b'm dolor si'
'''

#2 mmap write slice

import mmap
import shutil

# make a copy
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reversed = word[::-1]
print('Looking for   :', word)
print('Replacing with:', reversed)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # go to first

        loc = m.find(word)
        m[loc:loc + len(word)] = reversed
        m.flush()

        m.seek(0)  # go to first
        print('After :\n{}'.format(m.readline().rstrip()))

        f.seek(0)  # got to first
        print('File:\n{}'.format(f.readline().rstrip()))

'''RESULTS:
Looking for   : b'consectetuer'
Replacing with: b'reutetcesnoc'
Before:
b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
After :
b'Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.'
File:
Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.
'''

#3 write copy

import mmap
import shutil

# copy file
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reversed = word[::-1]

with open('lorem_copy.txt','r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
        print('Memory Before:\n{}'.format(
            m.readline().rstrip()))
        print('File Before  :\n{}\n'.format(
            f.readline().rstrip()))

        m.seek(0)  # go to first
        loc = m.find(word)
        m[loc:loc + len(word)] = reversed

        m.seek(0)  # go to first
        print('Memory After  :\n{}'.format(
            m.readline().rstrip()))

        f.seek(0)
        print('File After    :\n{}'.format(
            f.readline().rstrip()))

'''RESULTS:
Memory Before:
b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
File Before  :
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

Memory After  :
b'Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.'
File After    :
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
'''

#4 mmap regex
