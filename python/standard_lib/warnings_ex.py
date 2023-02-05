"""warnings about."""

#1 warnings warn

import warnings

'''
print('Before the warning')
warnings.warn('This is a warning message')
print('After the warning')

RESULTS:
Before the warning
<stdin>:9: UserWarning: This is a warning message
After the warning
'''

#2 warnings warn raise

import warnings

'''
warnings.simplefilter('error', UserWarning)

print('Before the warning')
warnings.warn('This is a warning message')
print('After the warning')

RESULTS:
Before the warning
Traceback (most recent call last):
  File "<stdin>", line 26, in <module>
UserWarning: This is a warning message
'''

#3 warnings filterwarnings message

import warnings

'''
warnings.filterwarnings('ignore', '.*do not.*',)

warnings.warn('Show this message')
warnings.warn('Do not show this message')

RESULTS:
<stdin>:42: UserWarning: Show this message
'''

#4 warnings showwarning

import warnings
import logging

'''
def send_warnings_to_log(message, category, filename, lineno,
        file=None, line=None):
    logging.warning(
            '%s:%s: %s:%s',
            filename, lineno,
            category.__name__, message,
    )

logging.basicConfig(level=logging.INFO)

old_showwarnig = warnings.showwarning
warnings.showwarning = send_warnings_to_log

warnings.warn('message')

RESULTS:
WARNING:root:<stdin>:69: UserWarning:message
'''

#5 warnings formatwarning

import warnings

'''
def warning_on_one_line(message, category, filename, lineno,
        file=None, line=None):
    return '-> {}:{}: {}:{}'.format(
            filename, lineno, category.__name__, message)

warnings.warn('Warning message, before')
warnings.formatwarning = warning_on_one_line
warnings.warn('Warning message, after')

RESULTS:
<stdin>:89: UserWarning: Warning message, before
-> <stdin>:91: UserWarning:Warning message, after
'''

#6 warnings warn stacklevel

#!/usr/bin/env python3
# encoding: utf-8

import warnings


def old_function():
    warnings.warn(
            'old_function() is deprecated, use new_function()',
            stacklevel=2)

def caller_of_old_function():
    old_function()


caller_of_old_function()

RESULTS:
<stdin>:108: UserWarning: old_function() is deprecated, use new_function()
