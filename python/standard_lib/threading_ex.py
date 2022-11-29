"""threading about."""

#1 simple

import threading

def worker():
    """Function of work flow."""
    print('Worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

'''RESULTS:
Worker
Worker
Worker
Worker
Worker
'''

#2 threading simple args

import threading


def worker(num):
    """Func of workflow."""
    print('Worker: %s' % num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

'''RESULTS:
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
'''

#3 threading names

import threading
import time
'''
def worker():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

def my_service():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.3)
    print(threading.current_thread().getName(), "Exiting")

t = threading.Thread(name="my_service", target=my_service)
w = threading.Thread(name="worker", target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()
'''
#4 threading names log

import logging
import threading
import time


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')

logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()

'''RESULTS:
[DEBUG] (worker    ) Starting
[DEBUG] (Thread-12 (worker)) Starting
[DEBUG] (my_service) Starting
<stdin>:56: DeprecationWarning: getName() is deprecated, get the name attribute instead
Thread-11 (worker) Exiting
worker Exiting
[DEBUG] (worker    ) Exiting
[DEBUG] (Thread-12 (worker)) Exiting
<stdin>:61: DeprecationWarning: getName() is deprecated, get the name attribute instead
my_service Exiting
[DEBUG] (my_service) Exiting
'''

#5 threading daemon join

import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(0.5)
#print('d.isAlive()', d.isAlive())
t.join()

#6 threading enumerate

import random
import threading
import time
import logging


def worker():
    """Func workflow."""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()

#7  threading subclass

import threading
import logging


class MyThread(threading.Thread):

    def run(self):
        logging.debug('runnig')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()

'''RESULTS:
[DEBUG] (Thread-15 ) runnig
[DEBUG] (Thread-16 ) runnig
[DEBUG] (Thread-17 ) runnig
[DEBUG] (Thread-18 ) runnig
[DEBUG] (Thread-19 ) runnig
'''

#8 threading subclass args

import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
    t.start()

'''RESULTS:
[DEBUG] (Thread-20 ) running with (0,) and {'a': 'A', 'b': 'B'}
[DEBUG] (Thread-21 ) running with (1,) and {'a': 'A', 'b': 'B'}
[DEBUG] (Thread-22 ) running with (2,) and {'a': 'A', 'b': 'B'}
[DEBUG] (Thread-23 ) running with (3,) and {'a': 'A', 'b': 'B'}
[DEBUG] (Thread-24 ) running with (4,) and {'a': 'A', 'b': 'B'}
'''

#9 threading timer

import threading
import time
import logging


def delayed():
    logging.debug('worker running')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

t1 = threading.Timer(0.3, delayed)
t1.setName('t1')
t2 = threading.Timer(0.3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(0.2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')

'''RESULTS:
<stdin>:258: DeprecationWarning: setName() is deprecated, set the name attribute instead
<stdin>:260: DeprecationWarning: setName() is deprecated, set the name attribute instead
[DEBUG] (MainThread) starting timers
<stdin>:266: DeprecationWarning: getName() is deprecated, get the name attribute instead
[DEBUG] (MainThread) waiting before canceling t2
<stdin>:268: DeprecationWarning: getName() is deprecated, get the name attribute instead
[DEBUG] (MainThread) canceling t2
[DEBUG] (MainThread) done
[DEBUG] (t1        ) worker running
'''

#10 threading event

import logging
import threading
import time

def wait_for_event(e):
    """Wait set event before all."""
    logging.debug('wait_for_event starting')

    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    """Wait t sec and stop by time-out."""
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,),
)
t1.start()

t2 = threading.Thread(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.3)
e.set()
logging.debug('Event is set')

'''RESULTS:
[DEBUG] (block     ) wait_for_event starting
[DEBUG] (nonblock  ) wait_for_event_timeout starting
[DEBUG] (MainThread) Waiting before calling Event.set()
[DEBUG] (t1        ) worker running
[DEBUG] (MainThread) Event is set
[DEBUG] (block     ) event set: True
[DEBUG] (nonblock  ) event set: True
[DEBUG] (nonblock  ) processing event
'''

#11 defence for one asc from both obj with Lock

import logging
import random
import threading
import time


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

'''RESULTS:
[DEBUG] (Thread-28 (worker)) Sleeping 0.54
[DEBUG] (MainThread) Waiting for worker threads
[DEBUG] (Thread-28 (worker)) Waiting for lock
[DEBUG] (Thread-28 (worker)) Acquired lock
[DEBUG] (Thread-28 (worker)) Sleeping 0.41
[DEBUG] (Thread-27 (worker)) Waiting for lock
[DEBUG] (Thread-27 (worker)) Acquired lock
[DEBUG] (Thread-27 (worker)) Sleeping 0.03
[DEBUG] (Thread-27 (worker)) Waiting for lock
[DEBUG] (Thread-27 (worker)) Acquired lock
[DEBUG] (Thread-27 (worker)) Done
[DEBUG] (Thread-28 (worker)) Waiting for lock
[DEBUG] (Thread-28 (worker)) Acquired lock
[DEBUG] (Thread-28 (worker)) Done
[DEBUG] (MainThread) Counter: 4
'''

#12 threading lock noblock

import logging
import threading
import time


def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',
                              num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired',
                              num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
holder = threading.Thread(
        target=lock_holder,
        args=(lock,),
        name='LockHolder',
        daemon=True,
)
holder.start()

worker = threading.Thread(
        target=worker,
        args=(lock,),
        name='Worker',
)
worker.start()

'''RESULTS:
[DEBUG] (LockHolder) Starting
[DEBUG] (LockHolder) Holding
[DEBUG] (Worker    ) Starting
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 1: Acquired
[DEBUG] (LockHolder) Holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 2: Not acquired
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 3: Acquired
[DEBUG] (LockHolder) Holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 4: Not acquired
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 5: Acquired
[DEBUG] (Worker    ) Done after 5 iterations
'''

#13 threading lock reacquire

import threading

lock = threading.Lock()
print()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

'''RESULTS:  # interesting effect with sum of above code
First try : True
Second try: False
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 1: Acquired
[DEBUG] (LockHolder) Holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 2: Not acquired
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 3: Acquired
[DEBUG] (LockHolder) Holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 4: Not acquired
[DEBUG] (LockHolder) Not holding
[DEBUG] (Worker    ) Trying to acquire
[DEBUG] (Worker    ) Iteration 5: Acquired
[DEBUG] (Worker    ) Done after 5 iterations
'''

#14 threading rlock

import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

#15 threading lock with <with>

import threading
import logging


def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

''EXPECTED RESULTS:
(Thread-1  ) Lock acquired via with
(Thread-2  ) Lock acquired directly
'''

#16 threading condition

import logging
import threading
import time


def consumer(cond):
    """Wait and then use resource."""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


def producer(cond):
    """Set resource for use."""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s (%threadName)-2a) %(message)s',
)

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer,
        args=(condition,))
c2 = threading.Thread(name='c2', target=consumer,
        args=(condition,))
p = threading.Thread(name='p', target=producer,
        args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)

'''EXPECTED RESULTS:
2016-07-10 10:45:28,170 (c1) Starting consumer thread
2016-07-10 10:45:28,376 (c2) Starting consumer thread
2016-07-10 10:45:28,581 (p) Starting producer thread
2016-07-10 10:45:28,581 (p) Makeing resource available
                    582 (c1) Resource is available to consumer
                    582 (c2) Resource is available to consumer
'''

