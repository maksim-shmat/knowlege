"""More about threading."""

#1 threading barrier

import threading
import time
'''
def worker(barrier):
    print(threading.current_thread().name,
            'waiting for barrier with {} others'.format(
                barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'after barrier',
            worker_id)

NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS)

threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()

RESULTS:
worker-0 starting
worker-0 waiting for barrier with 0 others
worker-1 starting
worker-1 waiting for barrier with 1 others
worker-2 starting
worker-2 waiting for barrier with 2 others
worker-2 after barrier 2
worker-0 after barrier 0
worker-1 after barrier 1
'''

#2 threading barrier abort

import threading
import time
'''
def worker(barrier):
    print(threading.current_thread().name,
            'waiting for barrier with {} others'.format(
                barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier',
                worker_id)

NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()

RESULTS:
worker-0 starting
worker-0 waiting for barrier with 0 others
worker-1 starting
worker-1 waiting for barrier with 1 others
worker-2 starting
worker-2 waiting for barrier with 2 others
worker-0 aborting
worker-1 aborting
worker-2 aborting
'''

#3 semaphore for 2 thread only

import logging
import random
import threading
import time

'''
class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def  worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(
            target=worker,
            name=str(i),
            args=(s, pool),
    )
    t.start()

RESULTS:
2022-11-30 03:11:24,368 (0 ) Waiting to join the pool
<stdin>:130: DeprecationWarning: getName() is deprecated, get the name attribute instead
2022-11-30 03:11:24,368 (0 ) Running: ['0']
2022-11-30 03:11:24,369 (1 ) Waiting to join the pool
2022-11-30 03:11:24,369 (1 ) Running: ['0', '1']
2022-11-30 03:11:24,369 (2 ) Waiting to join the pool
2022-11-30 03:11:24,369 (3 ) Waiting to join the pool
2022-11-30 03:11:24,469 (0 ) Running: ['1']
2022-11-30 03:11:24,469 (2 ) Running: ['1', '2']
2022-11-30 03:11:24,470 (1 ) Running: ['2']
2022-11-30 03:11:24,470 (3 ) Running: ['2', '3']
2022-11-30 03:11:24,570 (2 ) Running: ['3']
2022-11-30 03:11:24,570 (3 ) Running: []
'''

#4 local() close data for other threads

import random
import threading
import logging

'''
def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

local_data = threading.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

RESULTS:
(MainThread) No value yet
(MainThread) value=1000
(Thread-1 (worker)) No value yet
(Thread-1 (worker)) value=58
(Thread-2 (worker)) No value yet
(Thread-2 (worker)) value=7
'''

#5 threading local defaults

import random
import threading
import logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


class MyLocal(threading.local):

    def __init__(self, value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value


logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
)

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

'''RESULTS:
(MainThread) Initializing <__main__.MyLocal object at 0x7f5fcc5da200>
(MainThread) value=1000
(Thread-1 (worker)) Initializing <__main__.MyLocal object at 0x7f5fcc5da200>
(Thread-1 (worker)) value=1000
(Thread-1 (worker)) value=71
(Thread-2 (worker)) Initializing <__main__.MyLocal object at 0x7f5fcc5da200>
(Thread-2 (worker)) value=1000
(Thread-2 (worker)) value=5
'''
