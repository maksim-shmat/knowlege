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

#7 os cwd example

import os

'''
print('Starting:', os.getcwd())

print('Moving up one:', os.pardir)
os.chdir(os.pardir)

print('After move:', os.getcwd())

RESULTS:
Starting: /home/jack/django2/knowlege/python
Moving up one: ..
After move: /home/jack/django2/knowlege
'''

#8 simple run command, os system example

import os

'''
# simple cmd
os.system('pwd')

RESULTS:
/home/jack/django2/knowlege/python
'''

#9 os system background

import os
import time

'''
print('Calling...')
time.sleep(5)

print('Sleeping...')
time.sleep(5)
'''

#10 os fork example

import os

'''
pid = os.fork()

if pid:
    print('Child process id:', pid)
else:
    print('I am the child')

RESULTS:
Child process id: 1329530
I am the child
'''

#11 os kill example

import os
import signal
import time

'''
def signal_usr1(sinnum, frame):
    "Callback function for signal."""
    pid = os.getpid()
    print('Received USR1 in process {}'.format(pid))

print('Forking...')
child_pid = os.fork()
if child_pid:
    print('PARENT: Pausing before sending signal...')
    time.sleep(1)
    print('PARENT: Signaling {}'.format(child_pid))
    os.kill(child_pid, signal.SIGUSR1)
else:
    print('CHILD: Setting up signal handler')
    signal.signal(signal.SIGUSR1, signal_usr1)
    print('CHILD: Pausing to wait for signal')
    time.sleep(5)

RESULTS:
Forking...
PARENT: Pausing before sending signal...
CHILD: Setting up signal handler
CHILD: Pausing to wait for signal
PARENT: Signaling 1329955
Received USR1 in process 1329955
'''

#12 os wait() for wait how any daughters process is stopped

import os
import sys
import time

'''
for i in range(2):
    print('PARENT {}: Forking {}'.format(os.getpid(), i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER {}: Starting'.format(i))
        time.sleep(2 + i)
        print('WORKER {}: Finishing'.format(i))
        sys.exit(i)

for i in range(2):
    print('PARENT: Waiting for {}'.format(i))
    done = os.wait()
    print('PARENT: Child done:', done)

RESULTS:
PARENT 1330729: Forking 0
PARENT 1330729: Forking 1
WORKER 0: Starting
PARENT: Waiting for 0
WORKER 1: Starting
WORKER 0: Finishing
PARENT: Child done: (1330730, 0)
PARENT: Waiting for 1
WORKER 1: Finishing
PARENT: Child done: (1330731, 256)
'''

#13 os waitpid example
