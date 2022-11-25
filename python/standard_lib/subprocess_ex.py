"""subprocess about."""

#1 subprocess os system

import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)

'''RESULTS:
file1.py
file2.py
returncode: 0
'''

#2
