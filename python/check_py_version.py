"""Script for check your current Python version."""

import sys

sys.version_info
if sys.version_info > (3, 8): # if 3.8 print 'Do'
    print('Do')
else: # else print 'Install new versiojn'
    print('Install new version')
    
