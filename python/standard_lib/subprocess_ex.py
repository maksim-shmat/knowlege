"""subprocess about."""

#1 subprocess os system

import subprocess
'''
completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)

RESULTS:
file1.py
file2.py
returncode: 0
'''

#2 subprocess shell variable

import subprocess
'''
completed1 = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

RESULTS:
/home/jack
returncode: 0
'''

#3 subprocess run check

import subprocess
'''
try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
RESULTS:
/home/jack
returncode: 0
'''

#4 subprocess run output

import subprocess
'''
completed = subprocess.run(
        ['ls', '-1'],
        stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)
'''
#5 subprocess run output error

import subprocess

try:
    completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )

'''RESULTS:
to stderr
ERROR: Command 'echo to stdout; echo to stderr 1>&2; exit 1' returned non-zero exit status 1.
'''

#6  subprocess run output error trap

try:
    completed = subprocess.run(
            'echo to stdout: echo to sterr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )
    print('Have {} bytes in stderr: {!r}'.format(
        len(completed.stderr),
        completed.stderr.decode('utf-8'))
    )

'''RESULTS:
returncode: 1
Have 0 bytes in stdout: ''
Have 25 bytes in stderr: 'to stdout: echo to sterr\n'
'''

#7 subprocess check output error trap output

import subprocess

try:
    output = subprocess.check_output(
            'echo to stdout; echo to stderr 1>&2',
            shell=True,
            stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('Have {} bytes in output: {!r}'.format(
        len(output),
        output.decode('utf-8'))
    )

'''RESULTS:
Have 20 bytes in output: 'to stdout\nto stderr\n'
'''

#8 How down output with DEVNULL

import subprocess

try:
    completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('stdout is {!r}'.format(completed.stdout))
    print('stderr is {!r}'.format(completed.stderr))

'''RESULTS:
returncode: 1
stdout is None
stderr is None
'''

#9 subprocess popen read

import subprocess

print('read:')
proc = subprocess.Popen(
        ['echo', '"to stdout"'],
        stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

'''RESULTS:
read:
stdout: '"to stdout"\n'
'''

#10 subprocess popen write

import subprocess

print('write:')
proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))

'''RESULTS:
write:
stdin: to stdin
'''

#11 combine subprocess popen

import subprocess

print('popen_combine:')

proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
)
msg = 'through stdin to stdout'.encode('utf-8')
stdout_value = proc.communicate(msg)[0].decode('utf-8')
print('pass through:', repr(stdout_value))

'''RESULTS:
popen_combine:
pass through: 'through stdin to stdout'
'''

#12 view both threads stdout and stderr

import subprocess

print('popen_both:')
proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
)

msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('pass through:', repr(stdout_value.decode('utf-8')))
print('stderr      :', repr(stderr_value.decode('utf-8')))

'''RESULTS:
popen_both:
pass through: 'through stdin to stdout'
stderr      : 'to stderr\n'
'''

#13 STDOUT against PIPE

import subprocess

print('popen_against:')
proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
)
msg = 'through stdin to stdout\n'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('combined output:', repr(stdout_value.decode('utf-8')))
print('stderr value   :', repr(stderr_value))

'''RESULTS:
popen_against:
combined output: 'through stdin to stdout\nto stderr\n'
stderr value   : None
'''

#14 conveyer
# thata code make: $ cat index.rst | grep "..literalinclude" | cut -f 3 -d:

import subprocess

cat = subprocess.Popen(
        ['cat', 'index.rst'],
        stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
        ['grep', '.. literalinclude::'],
        stdin=cat.stdout,
        stdout=subprocess.PIPE,
)

cut = subprocess.Popen(
        ['cut', '-f', '3', '-d:'],
        stdin=grep.stdout,
        stdout=subprocess.PIPE,
)

end_of_pipe = cut.stdout

print('Included files:')
for line in end_of_pipe:
    print(line.decode('utf-8').strip())

'''RESULTS:
Included files:
'''

#15 it use repeater.py 

import io
import subprocess

print('One line at a time:')
proc = subprocess.Popen(
        'python3 repeater.py',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
        proc.stdin,
        encoding='utf-8',
        line_buffering=True,  # send data when get <\n>
)
stdout = io.TextIOWrapper(
        proc.stdout,
        encoding='utf-8',
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())
remainder = proc.communicate()[0].decode('utf-8')
print(remainder)

print()
print('All output at once:')
proc = subprocess.Popen(
        'python3 repeater.py',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
        proc.stdin,
        encoding='utf-8',
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
stdin.flush()

output = proc.communicate()[0].decode('utf-8')
print(output)

'''RESULTS:
One line at a time:
repeater.py: starting
0
1
2
3
4
repeater.py: exiting


All output at once:
repeater.py: starting
repeater.py: exiting
0
1
2
3
4
'''

#16 signal_child.py

import os
import signal
import time
import sys

pid = os.getpid()
received = False


def signal_usr1(signum, frame):
    """Callback start when get signal."""

    global received
    received = True
    print('CHILD {:>6}: Received USR1'.format(pid))
    sys.stdout.flush()

print('CHILD {:>6}: Settig up signal handler'.format(pid))
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print('CHILD {:>6}: Pausing to wait for signal'.format(pid))
sys.stdout.flush()
time.sleep(3)

if not received:
    print('CHILD {:>6}: Never received signal'.format(pid))

'''RESULTS:
CHILD 118264: Settig up signal handler
CHILD 118264: Pausing to wait for signal
CHILD 118264: Never received signal
'''

#17 signal_parent.py

import os
import signal
import subprocess
import time
import sys
'''
proc = subprocess.Popen(['python3', 'signal_child.py'])
print('PARENT      : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
'''

#18 subprocess_signal1_parent_shell.py

import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name])
print('PARENT      : Pausing before signaling {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child {}'.format(proc.pid))
sys.stdout.flush()
os.kill(proc.pid,signal.SIGUSR1)
time.sleep(3)

#19 subprocess_signal_setpgrp.py

import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(
        os.getpid(), os.getpgrp()))
    sys.stdout.flush()

script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
        ['sh', script_file.name],
        preexec_fn=show_setting_prgrp,
)
print('PARENT      : Pausing before signaling {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling process group {}'.format(
    proc.pid))
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)
