"""Futures from concurrent about."""

#1 futures thread pool map

from concurrent import futures
import threading
import time

'''
def task(n):
    print('{}:sleeping {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n / 10)
    print('{}: done with {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
results = ex.map(task, range(5, 0, -1))
print('main: unprocessed results {}'.format(results))
print('main: waiting for real results')
real_results = list(results)
print('main: results: {}'.format(real_results))

RESULTS:
main: starting
ThreadPoolExecutor-0_0:sleeping 5
ThreadPoolExecutor-0_1:sleeping 4
main: unprocessed results <generator object Executor.map.<locals>.result_iterator at 0x7f8347d67ed0>
main: waiting for real results
ThreadPoolExecutor-0_1: done with 4
ThreadPoolExecutor-0_1:sleeping 3
ThreadPoolExecutor-0_0: done with 5
ThreadPoolExecutor-0_0:sleeping 2
ThreadPoolExecutor-0_0: done with 2
ThreadPoolExecutor-0_0:sleeping 1
ThreadPoolExecutor-0_1: done with 3
ThreadPoolExecutor-0_0: done with 1
main: results: [0.5, 0.4, 0.3, 0.2, 0.1]
'''

#2 futures thread pool submit

from concurrent import futures
import threading
import time

'''
def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n / 10)
    print('{}: done with {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)
print('main: future: {}'.format(f))
print('main: waiting for results')
result = f.result()
print('main: result: {}'.format(result))
print('main: future after result: {}'.format(f))

RESULTS:
main: starting
ThreadPoolExecutor-1_0: sleeping 5
main: future: <Future at 0x7fa27064ffd0 state=running>
main: waiting for results
ThreadPoolExecutor-1_0: done with 5
main: result: 0.5
main: future after result: <Future at 0x7fa27064ffd0 state=finished returned float>
'''

#3 futures as completed

from concurrent import futures
import random
import time

'''
def task(n):
    time.sleep(random.random())
    return (n, n / 10)


ex = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

wait_for = [
        ex.submit(task, i)
        for i in range(5, 0, -1)
]

for f in futures.as_completed(wait_for):
    print('main: results: {}'.format(f.result()))

RESULTS:
main: starting
main: results: (2, 0.2)
main: results: (5, 0.5)
main: results: (3, 0.3)
main: results: (4, 0.4)
main: results: (1, 0.1)
'''

#4 futures future callback

from concurrent import futures
import time

'''
def task(n):
    print('{}: sleeping'.format(n))
    time.sleep(0.5)
    print('{}: done'.format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: error returned: {}'.format(
                fn.arg, error))
        else:
            result = fn.result()
            print('{}: value returned: {}'.format(
                fn.arg, result))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()

RESULTS:
main: starting
5: sleeping
5: done
5: value returned: 0.5
'''

#5 futures future callback cancel

from concurrent import futures
import time

'''
def task(n):
    print('{}: sleeping'.format(n))
    time.sleep(0.5)
    print('{}: done'.format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        print('{}: not canceled'.format(fn.arg))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    tasks = []

    for i in range(10, 0, -1):
        print('main: submitting {}'.format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print('main: did not cancel {}'.format(i))

    ex.shutdown()

RESULTS:
main: starting
main: submitting 10
10: sleeping
main: submitting 9
9: sleeping
main: submitting 8
main: submitting 7
main: submitting 6
main: submitting 5
main: submitting 4
main: submitting 3
main: submitting 2
main: submitting 1
1: canceled
2: canceled
3: canceled
4: canceled
5: canceled
6: canceled
7: canceled
8: canceled
main: did not cancel 9
main: did not cancel 10
10: done
10: not canceled
9: done
9: not canceled
'''

#6 futures future exception

from concurrent import futures

'''
def task(n):
    print('{}: starting'.format(n))
    raise ValueError('the value {} is not good'.format(n))


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)

error = f.exception()
print('main: error: {}'.format(error))

try:
    result = f.result()
except ValueError as e:
    print('main: saw error "{}" when accessing result'.format(e))

RESULTS:
main: starting
5: starting
main: error: the value 5 is not good
main: saw error "the value 5 is not good" when accessing result
'''

#7 futures context manager

from concurrent import futures

'''
def task(n):
    print(n)


with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)

print('main: done')

RESULTS:
main: starting
1
2
3
4
main: done
'''

#8 futures process pool map
