"""sched about."""

#1 sched_basic

import sched
import time

'''
scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('EVENT: {} elapsed={} name={}'.format(
        time.ctime(now), elapsed, name))

start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, print_event, ('first', start))
scheduler.enter(3, 1, print_event, ('second', start))

scheduler.run()

RESULTS:
START: Sun Jan 22 11:20:03 2023
EVENT: Sun Jan 22 11:20:05 2023 elapsed=2 name=first
EVENT: Sun Jan 22 11:20:06 2023 elapsed=3 name=second
'''

#2 sched overlap

import sched
import time

'''
scheduler = sched.scheduler(time.time, time.sleep)


def long_event(name):
    print('BEGIN EVENT :', time.ctime(time.time()), name)
    time.sleep(2)
    print('FINISH EVENT:', time.ctime(time.time()), name)

print('START:', time.ctime(time.time()))
scheduler.enter(2, 1, long_event, ('first',))
scheduler.enter(3, 1, long_event, ('second',))

scheduler.run()

RESULTS:
START: Sun Jan 22 11:24:20 2023
BEGIN EVENT : Sun Jan 22 11:24:22 2023 first
FINISH EVENT: Sun Jan 22 11:24:24 2023 first
BEGIN EVENT : Sun Jan 22 11:24:24 2023 second
FINISH EVENT: Sun Jan 22 11:24:26 2023 second
'''

#3 
