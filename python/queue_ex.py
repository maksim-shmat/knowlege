"""Queue about."""

'''
#1 Queues default type is FIFO

import queue

q = queue.Queue()

for x in range(5):
    q.put(x)
    for x in range(5):
        print(q.get(x))

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
        print(q.get())

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

#5 
