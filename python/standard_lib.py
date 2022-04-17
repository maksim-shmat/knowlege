"""Standard library modules about."""

# http://docs.python.org/py3k/library/index.html

#1 sys

import sys

print(sys.version_info)
# sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0)

print(sys.version_info[0] >= 3)
# True

#2 warnings

import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Need Python 3.0 minmium", RuntimeWarning)
else:
    print('Your version of Python is ok.')

#3 logging

import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),\
            os.getenv('HOMEPATH'), \
            'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print('Save log into: ', logging_file)

logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s : %(levelname)s : %(message)s',
        filename = logging_file,
        filemode = 'w',
)

#4
