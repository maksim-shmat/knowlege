"""os about."""

#1 os directories

import os

'''
dir_name = 'os_directories_example'

print('Creating', dir_name)
os.makedirs(dir_name)

file_name = os.path.join(dir_name, 'example.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
    f.write('example file')

print('Cleaning up')
os.unlink(file_name)
os.rmdir(dir_name)
'''

#2 mkdir() and rmdir() - one dir
#  makedirs() and removedirs() - full path

#3 os symlinks

import os

'''
link_name = '/tmp/' + os.path.basename(__file__)

print('Creating link {} -> {}'.format(link_name, __file__))
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print('Permissions:', oct(stat_info.st_mode))

print('Points to:', os.readlink(link_name))

# Clear
os.unlink(link_name)

RESULTS:
Creating link /tmp/<stdin> -> <stdin>
Permissions: 0o120777
Points to: <stdin>
'''

#4 mv is danger rename() and replace() is better, ORLY?

import glob
import os

'''
with open('rename_start.txt', 'w') as f:
    f.write('starting as rename_start.txt')

print('Starting:', glob.glob('rename*.txt'))

os.rename('rename_start.txt', 'rename_finish.txt')

print('After rename:', glob.glob('rename*.txt'))

with open('rename_new_contents.txt', 'w') as f:
    f.write('ending with contents of rename_new_contents.txt')

os.replace('rename_new_contents.txt', 'rename_finish.txt')

with open('rename_finish.txt', 'r') as f:
    print('After replace:', repr(f.read()))

for name in glob.glob('rename*.txt'):
    os.unlink(name)

RESULTS:
Starting: ['rename_start.txt']
After rename: ['rename_finish.txt']
After replace: 'ending with contents of rename_new_contents.txt'
'''

#5 os process user example

import os

'''
TEST_GID = 502  # change to real user
TEST_UID = 502


def show_user_info():
    print('User (acutal/effective)   : {} / {}'.format(
        os.getuid(), os.geteuid()))
    print('Group (actual/effective)  : {} / {}'.format(
        os.getgid(), os.getegid()))
    print('Actual Groups  :', os.getgroups())

print('BEFORE CHANGE:')
show_user_info()
print()

try:
    os.setegid(TEST_GID)
except OSError:
    print('ERROR: Could not change effective group. '
          'Return as root.')
else:
    print('CHANGE GROUP:')
    show_user_info()
    print()

try:
    os.seteuid(TEST_UID)
except OSError:
    print('ERROR: Could not change effective user. '
          'Return as root.')
else:
    print('CHANGE USER:')
    show_user_info()
    print()

RESULTS:
BEFORE CHANGE:
User (acutal/effective)   : 1001 / 1001
Group (actual/effective)  : 1001 / 1001
Actual Groups  : [4, 10, 24, 27, 30, 46, 118, 126, 998, 1001]

ERROR: Could not change effective group. Return as root.
ERROR: Could not change effective user. Return as root.

Need: $ sudo python3 os_process_user_example.py
'''

#6 os environ example

import os

'''
print('Initial value:', os.environ.get('TESTVAR', None))
print('Child process:')
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'

print()
print('Change value:', os.environ['TESTVAR'])
print('Child process:')
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print()
print('Removed value:', os.environ.get('TESTVAR', None))
print('Child process:')
os.system('echo $TESTVAR')

RESULTS:
Initial value: None
Child process:


Change value: THIS VALUE WAS CHANGED
Child process:
THIS VALUE WAS CHANGED

Removed value: None
Child process:
'''

#7 
