"""Queue about."""

"""
#1 Queues default type is FIFO(First In First out)

import queue

q = queue.Queue()

for x in range(5):
    q.put(x)
    for x in range(5):
        print(q.get(x))

#1.1 queue fifo
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
'''RESULTS:
0 1 2 3 4
'''

#2

import threading
import queue
import math

q = queue.Queue()
threads = []

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))
        q.task_done()

for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
    zahlen = [134000, 14, 5, 300, 98, 88, 11, 23]

    for item in zahlen:
        q.put(item)
        q.join()

        for i in range(5):
            q.put(None)

#3 Queues LIFO

import queue

q = queue.LifoQueue()
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    q.put(x)
while not q.empty():
    print(q.get(), end=' ')
print()
'''RESULTS:
4 3 2 1 0
'''

'''
#4 Prioritizing Queues

import queue

q = queue.PriorityQueue()
q.put((8, "Some string"))
q.put((1, 2023))
q.put((90, True))
q.put((2, 10.23))

while not q.empty():
    print(q.get())  # or print(q.get()[1])

#5 queue priority
import functools
import queue
import threading

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()

workers = [
        threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()

'''RESULTS:
New job: Mid-level job
New job: Low-level job
New job: Important job
<stdin>:132: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
Processing job: Important job
Processing job: Mid-level job
Processing job: Low-level job
'''
"""


