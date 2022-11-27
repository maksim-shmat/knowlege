"""signal about."""

#1 getsignal

import signal

def alarm_received(n, stack):
    return

signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = {
        getattr(signal, n): n
        for n in dir(signal)
        if n.startswith('SIG') and '_' not in n
}

for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print('{:<10} ({:2d}):'.format(name, s), handler)

'''RESULTS:
SIGHUP     ( 1): SIG_DFL
SIGINT     ( 2): <built-in function default_int_handler>
SIGQUIT    ( 3): SIG_DFL
SIGILL     ( 4): SIG_DFL
SIGTRAP    ( 5): SIG_DFL
SIGIOT     ( 6): SIG_DFL
SIGBUS     ( 7): SIG_DFL
SIGFPE     ( 8): SIG_DFL
SIGKILL    ( 9): SIG_DFL
SIGUSR1    (10): SIG_DFL
SIGSEGV    (11): SIG_DFL
SIGUSR2    (12): SIG_DFL
SIGPIPE    (13): SIG_IGN
SIGALRM    (14): <function alarm_received at 0x7fdfc318fd90>
SIGTERM    (15): SIG_DFL
SIGCLD     (17): SIG_DFL
SIGCONT    (18): SIG_DFL
SIGSTOP    (19): SIG_DFL
SIGTSTP    (20): SIG_DFL
SIGTTIN    (21): SIG_DFL
SIGTTOU    (22): SIG_DFL
SIGURG     (23): SIG_DFL
SIGXCPU    (24): SIG_DFL
SIGXFSZ    (25): SIG_IGN
SIGVTALRM  (26): SIG_DFL
SIGPROF    (27): SIG_DFL
SIGWINCH   (28): SIG_DFL
SIGPOLL    (29): SIG_DFL
SIGPWR     (30): SIG_DFL
SIGSYS     (31): SIG_DFL
SIGRTMIN   (34): SIG_DFL
SIGRTMAX   (64): SIG_DFL
'''

#2 signal alarm

import signal
import time


def receive_alarm(signum, stack):
    print('Alarm:', time.ctime())

# Call receive_alarm after 2 sec
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before:', time.ctime())
time.sleep(4)
print('After :', time.ctime())

'''RESULTS:
Before: Sat Nov 26 18:34:48 2022
Alarm: Sat Nov 26 18:34:50 2022
After : Sat Nov 26 18:34:52 2022
'''

#3 signal ignore, there Ctrl-C will be ignored, use other terminal and cmd:
# kill -USR1 <My PID> e.g. 348923

import signal
import os
import time

'''
def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My PID:', os.getpid())

signal.pause()

RESULTS:
My PID: 126981
^[[OExiting
'''

#4 signal and threads

import signal
import threading
import os
import time


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(
        num, threading.currentThread().name))

signal.signal(signal.SIGUSR1, signal_handler)
'''
def wait_for_signal():
    print('Waiting for signal in',
            threading.currentThread().name)
    signal.pause()
    print('Done waiting')

# Start thread how not will get signals
receiver = threading.Thread(
        target=wait_for_signal,
        name='receiver',
)
receiver.start()
time.sleep(0.1)

def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# Wait signal, but not way with this
print('Waiting for', receiver.name)
signal.alarm(2)
receiver.join()
'''

#5 signal threads alarm

import signal
import time
import threading

def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in',
            threading.currentThread().name)

signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    t_name = threading.currentThread().name
    print(time.ctime(), 'Setting alarm in', t_name)
    signal.alarm(1)
    print(time.ctime(), 'Sleeping in', t_name)

    time.sleep(3)
    print(time.ctime(), 'Done with sleep in', t_name)

# Start a thread, how not be get signals
alarm_thread = threading.Thread(
        target=use_alarm,
        name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)

# Wait signal(it not be)
print(time.ctime(), 'Waiting for', alarm_thread.name)
alarm_thread.join()

print(time.ctime(), 'Existing normally')

'''RESULTS:
Sat Nov 26 19:03:41 2022 Setting alarm in alarm_thread
Sat Nov 26 19:03:41 2022 Sleeping in alarm_thread
Sat Nov 26 19:03:41 2022 Waiting for alarm_thread
<stdin>:157: DeprecationWarning: currentThread() is deprecated, use current_thread() instead
Sat Nov 26 19:03:42 2022 Alarm in MainThread
Sat Nov 26 19:03:44 2022 Done with sleep in alarm_thread
Sat Nov 26 19:03:44 2022 Existing normally
'''
