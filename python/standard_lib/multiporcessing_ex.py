"""multiprocessing about."""

#1 multiprocessing simple

import multiprocessing


def worker():
    print('Worker')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
'''
RESULTS:
Worker
Worker
Worker
Worker
Worker
'''

#2 multiprocessing simple args (args need serialize with pickle) orly?

import multiprocessing


def worker(num):
    print('Worker:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
'''
RESULTS:
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
'''

#3 multiprocessing names

import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'Starting')

    time.sleep(2)
    print(name, 'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(
            name='my_service',
            target=my_service,
    )
    worker_1 = multiprocessing.Process(
            name='worker 1',
            target=worker,
    )
    worker_2 = multiprocessing.Process(  # default name
            target=worker,
    )

    worker_1.start()
    worker_2.start()
    service.start()
'''
RESULTS:
worker 1 Starting
Process-3 Starting
my_service Starting
Process-3 Exiting
worker 1 Exiting
my_service Exiting
'''

#4 multiprocessing daemon. Check daemons: $ ps

import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
            name='daemon',
            target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
            name='non_daemon',
            target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
'''
RESULTS:
Starting: daemon 264446
Starting: non_daemon 264447
Exiting : non_daemon 264447
'''

#5 multiprocessing daemon join

import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    time.sleep(2)
    print('Exiting :', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    print('Exiting :', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
            name='daemon',
            target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
            name='non-daemon',
            target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()

'''RESULTS:
Starting: non-daemon
Exiting : non-daemon
my_service Exiting
Exiting : daemon
'''

#6 multiprocessing deamon join timeout

import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    time.sleep(2)
    print('Exiting :', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    print('Exiting :', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
            name='daemon',
            target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
            name='non-daemon',
            target=non_daemon,
    )
    n.daemon = False

    d.start()
    n.start()

    d.join(1)
    print('d.is_alive()', d.is_alive())
    n.join()

'''RESULTS:
Starting: non-daemon
Exiting : non-daemon
d.is_alive() True
'''

#7 multiprocessing terminate

import multiprocessing
import time


def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')


if __name__ == '__main__':
    p =multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    p.terminate()
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())

'''RESULTS:
BEFORE: <Process name='Process-20' parent=266678 initial> False
DURING: <Process name='Process-20' pid=266700 parent=266678 started> True
TERMINATED: <Process name='Process-20' pid=266700 parent=266678 started> True
JOINED: <Process name='Process-20' pid=266700 parent=266678 stopped exitcode=-SIGTERM> False
'''

#8 multiprocessing exitcode

import multiprocessing
import sys
import time


def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError('There was an error!')


def terminated():
    time.sleep(3)


if __name__ == '__main__':
    jobs = []
    funcs = [
            exit_error,
            exit_ok,
            return_value,
            raises,
            terminated,
    ]
    for f in funcs:
        print('Starting process for', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))

'''RESULTS:
Starting process for exit_error
Starting process for exit_ok
Starting process for return_value
Starting process for raises
Starting process for terminated
     exit_error.exitcode = 1
        exit_ok.exitcode = 0
   return_value.exitcode = 0
Process raises:
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "<stdin>", line 288, in raises
RuntimeError: There was an error!
         raises.exitcode = 1
     terminated.exitcode = -15
'''

#9 multiprocessing log to stderr

import multiprocessing
import logging
import sys


def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

'''RESULTS:
[INFO/Process-26] child process calling self.run()
Doing some work
[INFO/Process-26] process shutting down
[DEBUG/Process-26] running all "atexit" finalizers with priority >= 0
[DEBUG/Process-26] running the remaining "atexit" finalizers
[INFO/Process-26] process exiting with exitcode 0
[INFO/MainProcess] process shutting down
[DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
[INFO/MainProcess] calling terminate() for daemon daemon
[INFO/MainProcess] calling join() for process daemon
[DEBUG/MainProcess] running the remaining "atexit" finalizers
'''

#10 multiprocessing get_logger()
