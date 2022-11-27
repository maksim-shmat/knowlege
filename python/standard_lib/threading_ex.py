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

#6
