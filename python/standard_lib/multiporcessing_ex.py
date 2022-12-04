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

'''
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

RESULTS:
Starting: non-daemon
Exiting : non-daemon
my_service Exiting
Exiting : daemon
'''

#6 multiprocessing deamon join timeout

import multiprocessing
import time
import sys

'''
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

RESULTS:
Starting: non-daemon
Exiting : non-daemon
d.is_alive() True
'''

#7 multiprocessing terminate

import multiprocessing
import time

'''
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

RESULTS:
BEFORE: <Process name='Process-20' parent=266678 initial> False
DURING: <Process name='Process-20' pid=266700 parent=266678 started> True
TERMINATED: <Process name='Process-20' pid=266700 parent=266678 started> True
JOINED: <Process name='Process-20' pid=266700 parent=266678 stopped exitcode=-SIGTERM> False
'''

#8 multiprocessing exitcode

import multiprocessing
import sys
import time

'''
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

RESULTS:
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

'''
def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

RESULTS:
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

import multiprocessing
import logging
import sys

'''
def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
'''
#11 multiprocessing subcalss

import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()

'''
RESULTS:
In Worker-16
In Worker-17
In Worker-18
In Worker-19
In Worker-20
worker 1 Exiting
Process-13 Exiting
my_service Exiting
'''

#12 multiprocessing queue (send message to process)

import multiprocessing


class MyFancyClass:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Doing something fancy in {} for {}!'.format(
            proc_name, self.name))


def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('God of Fancy'))

    # Wait how process is stoped
    queue.close()
    queue.join_thread()
    p.join()

#13 multiprocessing producer consumer

import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Stop doing insertion
                print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # work imitation
        return '{self.a} * {self.b} = {product}'.format(
                self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


if __name__ == '__main__':
    # make a queue
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creating {} consumer'.format(num_consumers))
    consumers = [
            Consumer(tasks, results)
            for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    # Put tasks into queue
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add stop work insertion for every consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait how all tasks are complete
    tasks.join()

    # Return results
    while num_jobs:
        result = results.get()
        print('Results:', results)
        num_jobs -= 1

'''
RESULTS:
Creating 16 consumer
Consumer-23: 1 * 1
Consumer-22: 0 * 0
Consumer-24: 2 * 2
Consumer-25: 3 * 3
Consumer-26: 4 * 4
Consumer-27: 5 * 5
Consumer-29: 7 * 7
Consumer-28: 6 * 6
Consumer-30: 8 * 8
Consumer-31: 9 * 9
Consumer-32: Exiting
Consumer-33: Exiting
Consumer-34: Exiting
Consumer-35: Exiting
Consumer-36: Exiting
Consumer-37: Exiting
Consumer-22: Exiting
Consumer-25: Exiting
Consumer-27: Exiting
Consumer-29: Exiting
Consumer-26: Exiting
Consumer-28: Exiting
Consumer-24: Exiting
Consumer-31: Exiting
Consumer-23: Exiting
Consumer-30: Exiting
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
Results: <multiprocessing.queues.Queue object at 0x7f26a154e290>
worker 1 Exiting
Process-13 Exiting
my_service Exiting
'''

#14 multiprocessing event

import multiprocessing
import time


def wait_for_event(e):
    """Wait event before do something."""
    print('wait_for_event: starting')
    e.wait()
    print('wait_for_event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e, t):
    """Wait t seconds and then stop with time-out."""
    print('wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
            name='block',
            target=wait_for_event,
            args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
            name='nonblock',
            target=wait_for_event_timeout,
            args=(e, 2),
    )
    w2.start()

    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')

'''
RESULTS:
main: waiting before calling Event.set()
wait_for_event: starting
wait_for_event_timeout: e.is_set()-> False
worker 1 Exitinga        # tprrough i.e. wait-wait
Exiting : daemon 273314  # from other code
Process-13 Exiting       # other from above
my_service Exiting       # The princess is in another castle
main: event is set
wait_for_event: e.is_set()-> True
'''

#15 multiprocessing lock

import multiprocessing
import sys

def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')

def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()


lock = multiprocessing.Lock()
w = multiprocessing.Process(
        target=worker_with,
        args=(lock, sys.stdout),
)
nw = multiprocessing.Lock()
w = multiprocessing.Process(
        target=worker_with,
        args=(lock, sys.stdout),
)
nw = multiprocessing.Process(
        target=worker_no_with,
        args=(lock, sys.stdout),
)

w.start()
nw.start()

w.join()
nw.join()

'''
RESULTS:
Lock acquired via with
Lock acquired directly
'''

#16 multiprocessing condition. Operations sync.

import multiprocessing
import time


def stage_1(cond):
    """Do first chunk of job and send message to stage_2 for next step."""
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        print('{} done and ready for stage 2'.format(name))
        cond.notify_all()


def stage_2(cond):
    """Wait how stage_1 is complete."""
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        cond.wait()
        print('{} running'.format(name))


if __name__ == '__main__':
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name='s1',
                                 target=stage_1,
                                 args=(condition,))
    s2_clients = [
            multiprocessing.Process(
                name='stage_2[{}]'.format(i),
                target=stage_2,
                args=(condition,),
            )
            for i in range(1, 3)
    ]
    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()

    s1.join()
    for c in s2_clients:
        c.join()

'''
RESULTS:
Starting stage_2[1]
Starting stage_2[2]
Starting s1
s1 done and ready for stage 2
stage_2[1] running
stage_2[2] running
'''

#17 multiprocessing semaphore

import random
import multiprocessing
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print('Activating {} now running {}'.format(
            name, pool))
        time.sleep(random.random())
        pool.makeInactive(name)


if __name__ =='__main__':
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [
            multiprocessing.Process(
                target=worker,
                name=str(i),
                args=(s, pool),
            )
            for i in range(10)
    ]

    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print('Now running {}'.format(pool))
        if alive == 0:
            # All tasks is complete
            break

'''
RESULTS:
Activating 0 now running ['0']
Activating 1 now running ['0', '1', '2']
Activating 2 now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Activating 3 now running ['0', '1', '3']
Activating 4 now running ['0', '3', '4']
Activating 5 now running ['3', '4', '5']
Now running ['3', '4', '5']
Now running ['3', '5', '6']
Activating 6 now running ['3', '5', '6']
Now running ['3', '5', '6']
Activating 7 now running ['5', '6', '7']
Now running ['5', '6', '7']
Now running ['5', '6', '7']
Activating 8 now running ['6', '7', '8']
Activating 9 now running ['6', '8', '9']
Now running ['6', '8', '9']
Now running ['8', '9']
Now running ['8', '9']
Now running []
'''

#18 multiprocessing manager dict

import multiprocessing


def worker(d, key, value):
    d[key] = value


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
            multiprocessing.Process(
                target=worker,
                args=(d, i, i * 2),
            )
            for i in range(10)
    ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:', d)

'''
RESULTS:
Results: {1: 2, 0: 0, 2: 4, 3: 6, 4: 8, 6: 12, 7: 14, 9: 18, 5: 10, 8: 16}
'''

#19 multiprocessing namespaces

import multiprocessing

def producer(ns, event):
    ns.value = 'This is the value'
    event.set()


def consumer(ns, event):
    try:
        print('Before event: {}'.format(ns.value))
    except Exception as err:
        print('Before event, error:', str(err))
    event.wait()
    print('After event:', ns.value)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    p = multiprocessing.Process(
            target=producer,
            args=(namespace, event),
    )
    c = multiprocessing.Process(
            target=consumer,
            args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()

'''
RESULTS:
Before event, error: 'Namespace' object has no attribute 'value'
After event: This is the value
'''

#20 Join list encore for add to namespace, other it don't work

import multiprocessing


def producer(ns, event):
    # Not Reload Global Value!
    ns.my_list.append('This is the value')
    event.set()


def consumer(ns, event):
    print('Before event:', ns.my_list)
    event.wait()
    print('After event :', ns.my_list)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

    event = multiprocessing.Event()
    p = multiprocessing.Process(
            target=producer,
            args=(namespace, event),
    )
    c = multiprocessing.Process(
            target=consumer,
            args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()

'''
RESULTS:
Before event: []
After event : []
'''

#21 multiprocessing pool

import multiprocessing


def do_calculation(data):
    return data * 2


def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    inputs = list(range(10))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
            processes=pool_size,
            initializer=start_process,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # no more tasks
    pool.join()

    print('Pool    :', pool_outputs)

'''
RESULTS:
Input   : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Built-in: <map object at 0x7f7ec9ef7eb0>  # EXPECTED RESULT: [0, 2, 4, 6, 8,
                                                              10, 12, 14, 16,
                                                              18]
Starting ForkPoolWorker-74
Starting ForkPoolWorker-75
Starting ForkPoolWorker-76
Starting ForkPoolWorker-77
Starting ForkPoolWorker-78
Starting ForkPoolWorker-79
Starting ForkPoolWorker-80
Starting ForkPoolWorker-81
Starting ForkPoolWorker-82
Starting ForkPoolWorker-83
Starting ForkPoolWorker-84
Starting ForkPoolWorker-85
Starting ForkPoolWorker-86
Starting ForkPoolWorker-87
Starting ForkPoolWorker-88
Starting ForkPoolWorker-89
Pool    : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''

#22 multiprocessing pool max tasks per child

import multiprocessing


def do_calculation(data):
    return data * 2

def start_process():
    print('Starting', multiprocessing.current_process().name)


if __name__ == '__main__':
    inputs = list(range(10))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
            processes=pool_size,
            initializer=start_process,
            maxtasksperchild=2,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    pool.join()

    print('Pool    :', pool_outputs)

'''
RESULTS:
Input   : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Built-in: <map object at 0x7f0c0edb0250>
Starting ForkPoolWorker-90
Starting ForkPoolWorker-91
Starting ForkPoolWorker-92
Starting ForkPoolWorker-93
Starting ForkPoolWorker-94
Starting ForkPoolWorker-95
Starting ForkPoolWorker-96
Starting ForkPoolWorker-97
Starting ForkPoolWorker-98
Starting ForkPoolWorker-99
Starting ForkPoolWorker-100
Starting ForkPoolWorker-101
Starting ForkPoolWorker-102
Starting ForkPoolWorker-103
Starting ForkPoolWorker-104
Starting ForkPoolWorker-105
Pool    : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''

#23 
