"""asyncio about."""


import asyncio

'''
async def coroutine():
    print('in coroutine')


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()


RESULTS:
<stdin>:11: DeprecationWarning: There is no current event loop
starting coroutine
entering event loop
in coroutine
closing event loop
'''

#2 asyncio coroutine return

import asyncio

'''
async def coroutine():
    print('in coroutine')
    return 'result'


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(coroutine())
    print('it returned: {!r}'.format(return_value))
finally:
    event_loop.close()


RESULTS:
<stdin>:40: DeprecationWarning: There is no current event loop
in coroutine
it returned: 'result'
'''

#3 asyncio coroutine chain

import asyncio

'''
async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))
finally:
    event_loop.close()

RESULTS:
<stdin>:78: DeprecationWarning: There is no current event loop
in outer
waiting for result1
in phase1
waiting for result2
in phase2
return value: ('result1', 'result2 derived from result1')
'''

#4 asyncio generator

import asyncio

'''
@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for result1')
    result1 = yield from phase1()
    print('waiting for result2')
    result2 = yield from phase2(result1)
    return (result1, result2)


@asyncio.coroutine
def phase1():
    print('in phase1')
    return 'result1'


@asyncio.coroutine
def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))
finally:
    event_loop.close()

RESULTS:
<stdin>:101: DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
<stdin>:111: DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
<stdin>:117: DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
<stdin>:122: DeprecationWarning: There is no current event loop
in outer
waiting for result1
in phase1
waiting for result2
in phase2
return value: ('result1', 'result2 derived from result1')
'''

#5 asyncio call soon

import asyncio
import functools

'''
def callback(arg, *, kwarg='default'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()

RESULTS:
<stdin>:161: DeprecationWarning: There is no current event loop
entering event loop
registering callbacks
callback invoked with 1 and default
callback invoked with 2 and not default
closing event loop
'''

#6 asyncio call later

import asyncio

'''
def callback(n):
    print('callback {} invoked'.format(n))


async def main(loop):
    print('registering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()

RESULTS:
entering event loop
registering callbacks
callback 3 invoked
callback 2 invoked
callback 1 invoked
closing event loop
'''

#7 asyncio call at global clock

import asyncio
import time

'''
def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop time: {}'.format(now))

    print('registering callbacks')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()

RESULTS:
<stdin>:236: DeprecationWarning: There is no current event loop
entering event loop
clock time: 1670377563.727475
loop time: 256750.725657456
registering callbacks
callback 3 invoked at 256750.725708036
callback 2 invoked at 256750.82597814
callback 1 invoked at 256750.926417026
closing event loop
'''

#8 asyncio <Future> event loop

import asyncio

'''
def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('scheduling mark_done')
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print('returned result: {!r}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

print('future result: {!r}'.format(all_done.result()))

RESULTS:
<stdin>:266: DeprecationWarning: There is no current event loop
<stdin>:268: DeprecationWarning: There is no current event loop
scheduling mark_done
entering event loop
setting future result to 'the result'
returned result: 'the result'
closing event loop
future result: 'the result'
'''

#9 asynciio future await


import asyncio

'''
def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()

    print('scheduling mark_done')
    loop.call_soon(mark_done, all_done, 'the result')

    result = await all_done
    print('returned result: {!r}'.format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:314: DeprecationWarning: There is no current event loop
scheduling mark_done
setting future result to 'the result'
returned result: 'the result'
'''

#10 asyncio future callback

import asyncio
import functools

'''
def callback(future, n):
    print('{}: future done: {}'.format(n, future.result()))


async def register_callbacks(all_done):
    print('registering callbacks on future')
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    await register_callbacks(all_done)
    print('setting result of future')
    all_done.set_result('the result')


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()

RESULTS:
<stdin>:349: DeprecationWarning: There is no current event loop
<stdin>:351: DeprecationWarning: There is no current event loop
registering callbacks on future
setting result of future
1: future done: the result
2: future done: the result
'''

#11 asyncio create task

import asyncio

'''
async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:384: DeprecationWarning: There is no current event loop
creating task
waiting for <Task pending name='Task-2' coro=<task_func() running at <stdin>:370>>
in task_func
task completed <Task finished name='Task-2' coro=<task_func() done, defined at <stdin>:370> result='the result'>
return value: 'the result'
'''

#12 asyncio cancel task

import asyncio

'''
async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())

    print('canceling task')
    task.cancel()

    print('canceled task {!r}'.format(task))
    try:
        await task

    except asyncio.CancelledError:
        print('caught error from canceled task')
    else:
        print('task result: {!r}'.format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:426: DeprecationWarning: There is no current event loop
creating task
canceling task
canceled task <Task cancelling name='Task-2' coro=<task_func() running at <stdin>:404>>
caught error from canceled task
'''

#13 asyncio cancel task if cancel in waiting

import asyncio

'''
async def task_func():
    print('in task_func, sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise
    return 'the result'


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('main() also sees task as canceled')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:471: DeprecationWarning: There is no current event loop
creating task
in task_func, sleeping
in task_canceller
canceled the task
task_func was canceled
main() also sees task as canceled
'''

#14 asyncio ensure future

import asyncio

'''
async def wrapped():
    print('wrapped')
    return 'result'


async def inner(task):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    result = await task
    print('inner: task returned {!r}'.format(result))


async def starter():
    print('starter: creating task')
    task = asyncio.ensure_future(wrapped())
    print('starter: waiting for inner')
    await inner(task)
    print('starter: inner returned')

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(starter())
finally:
    event_loop.close()

RESULTS:
<stdin>:511: DeprecationWarning: There is no current event loop
entering event loop
starter: creating task
starter: waiting for inner
inner: starting
inner: waiting for <Task pending name='Task-2' coro=<wrapped() running at <stdin>:492>>
wrapped
inner: task returned 'result'
starter: inner returned
'''

#15 asyncio wait

import asyncio

'''
async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
            phase(i)
            for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('results {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

RESULTS:
<stdin>:561: DeprecationWarning: There is no current event loop
starting main
waiting for phases to complete
<stdin>:556: DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
in phase 1
in phase 2
in phase 0
done with phase 0
done with phase 1
done with phase 2
results ['phase 1 result', 'phase 0 result', 'phase 2 result']
'''

#16 wait() with timeout for don't completed tasks

import asyncio

'''
async def phase(i):
    print('in phase {}'.format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print('phase {} canceled'.format(i))
        raise
    else:
        print('done with phase {}'.format(i))
        return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
            phase(i)
            for i in range(num_phases)
    ]
    print('waiting 0.1 for phases to complete')
    completed, pending = await asyncio.wait(phases, timeout=0.1)
    print('{} completed and {} pending'.format(
        len(completed), len(pending),
    ))
    # don't completed tasks stop for no errors
    if pending:
        print('canceling tasks')
        for t in pending:
            t.cancel()
    print('exiting main')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

RESULTS:
<stdin>:616: DeprecationWarning: There is no current event loop
starting main
waiting 0.1 for phases to complete
<stdin>:605: DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
in phase 1
in phase 2
in phase 0
done with phase 0
1 completed and 2 pending
canceling tasks
exiting main
phase 1 canceled
phase 2 canceled
'''

#17 gather() for wait both operations

import asyncio

'''
async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    results = await asyncio.gather(
            phase1(),
            phase2(),
    )
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()

RESULTS:
<stdin>:667: DeprecationWarning: There is no current event loop
starting main
waiting for phases to complete
in phase1
in phase2
done with phase2
done with phase1
results: ['phase1 result', 'phase2 result']
'''

#18 asyncio as_completed

import asyncio

'''
async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
            phase(i)
            for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        results.append(answer)
    print('results: {!r}'.format(results))
    return results


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

RESULTS:
<stdin>:712: DeprecationWarning: There is no current event loop
starting main
waiting for phases to complete
in phase 2
in phase 1
in phase 0
done with phase 2
received answer 'phase 2 result'
done with phase 1
received answer 'phase 1 result'
done with phase 0
received answer 'phase 0 result'
results: ['phase 2 result', 'phase 1 result', 'phase 0 result']
'''

#19 asyncio lock

import asyncio
import functools

'''
def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coro1(lock):
    print('coro1 waiting for the lock')
    with await lock:
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coro2(lock):
    print('coro2 waiting for the lock')
    await lock
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def main(loop):
    # Make and get different locking
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    await lock.acquire()
    print('lock acquired: {}'.format(lock.locked()))

    # Make func callback for unlock
    loop.call_later(0.1, functools.partial(unlock, lock))

    # Start programs what need locking
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)]),


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:777: DeprecationWarning: There is no current event loop
acquiring the lock before starting coroutines
lock acquired: True
waiting for coroutines
<stdin>:774: DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
coro2 waiting for the lock
coro1 waiting for the lock
Task exception was never retrieved
future: <Task finished name='Task-2' coro=<coro2() done, defined at <stdin>:752> exception=TypeError("object Lock can't be used in 'await' expression")>
Traceback (most recent call last):
  File "<stdin>", line 754, in coro2
TypeError: object Lock can't be used in 'await' expression
Task exception was never retrieved
future: <Task finished name='Task-3' coro=<coro1() done, defined at <stdin>:745> exception=TypeError("object Lock can't be used in 'await' expression")>
Traceback (most recent call last):
  File "<stdin>", line 747, in coro1
TypeError: object Lock can't be used in 'await' expression
'''

#20 asyncio event

import asyncio
import functools

'''
def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


async def main(loop):
    # Make different event
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    loop.call_later(
            0.1, functools.partial(set_event, event)
    )

    await asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:839: DeprecationWarning: There is no current event loop
event start state: False
<stdin>:835: DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
coro2 waiting for event
coro1 waiting for event
setting event in callback
coro2 triggered
coro1 triggered
event end state: True
'''

#21 asyncio condition

import asyncio

'''
async def consumer(condition, n):
    with await condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('consumer {} triggered'.format(n))
    print('ending consumer {}'.format(n))


async def manipulate_condition(condition):
    print('starting manipulate_condition')

    # Pause for start consumers
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        with await condition:
            print('notifying {} consumers'.format(i))
            condition.notify(n=1)
        await asyncio.sleep(0.1)

    with await condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending manipulate_condition')


async def main(loop):
    # Make a condition
    condition = asyncio.Condition()

    # Make a list of tasks which folow after condition
    consumers = [
            consumer(condition, i)
            for i in range(5)
    ]

    # Make a task for use 'condition' value
    loop.create_task(manipulate_condition(condition))

    # Wait how consumers is end job
    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

RESULTS:
<stdin>:906: DeprecationWarning: There is no current event loop
<stdin>:903: DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
starting manipulate_condition
Task exception was never retrieved
future: <Task finished name='Task-3' coro=<consumer() done, defined at <stdin>:862> exception=TypeError("object Condition can't be used in 'await' expression")>
Traceback (most recent call last):
  File "<stdin>", line 863, in consumer
TypeError: object Condition can't be used in 'await' expression
Task exception was never retrieved
future: <Task finished name='Task-6' coro=<consumer() done, defined at <stdin>:862> exception=TypeError("object Condition can't be used in 'await' expression")>

EXPECTED RESULTS:
starting manipulate_condition
consumer 3 is waiting
consumer 1 is waiting
consumer 2 is waiting
consumer 0 is waiting
consumer 4 is waiting
notifying 1 consumer
consumer 3 triggered
ending consumer3
notifying 2 consumer
consumer 1 triggered
ending consumer 1
consumer 2 triggered
ending consumer 2
notifying remaining consumers
ending manipulate_condition
consumer 0 triggered
ending consumer 0
consumer 4 triggered
ending consumer 4
'''

#22 asyncio queue

import asyncio

'''
async def consumer(n, g):
    print('consumer {}: starting'.format(n))
    while True:
        print('consumer {}: has item {}'.format(n, item))
        item = await q.get()
        print('consumer {}: has item {}'.format(n, item))
        if item is None:
            # None - signal for stop working
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumer {}: ending'.format(n))


async def producer(q, num_workers):
    print('producer: starting')
    # Add tasks in queue for job imitation
    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))
    # Add None in queue as signals for customers stop working
    print('producer: adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(loop, num_consumers):
    # Make queue that producer blocked while customers suck data
    q = asyncio.Queue(maxsize=num_consumers)

    # Make agenda for tasks of custumers
    consumers = [
            loop.create_task(consumer(i, 1))
            for i in range(num_consumers)
    ]
    
    # Make agenda for tasks of producers
    prod = loop.create_task(producer(q, num_consumers))

    # Wait how under programs is stoped
    await asyncio.wait(consumers + [prod])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()

EXPECTED RESULTS:

consumer 0: starting
consumer 0: waiting for item
consumer 1: starting
consumer 1: waiting for item
producer: starting
producer: added task 0 to the queue
producer: added task 1 to the queue
consumer 0: has item 0
consumer 1: has item 1
producer: added task 2 to the queue
producer: added task 3 to the queue
consumer 0: waiting for item
consumer 0: has item 2
producer: added task 4 to the queue
consumer 1: waiting for item
consumer 1: has item 3
producer: added task 5 to the queue
producer: adding stop signals to the queue
consumer 0: waiting for item
consumer 0: has item 4
consumer 1: waitning for item
consumer 1: has item 5
producer: waiting for queue to empty
consumer 0: waiting for item
consumer 0: has item None
consumer 0: ending
consumer 1: waiting for item
consumer 1: ending
producer: ending
'''

# 23 asyncio echo server protocol

import asyncio
import logging
import sys

'''
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
                'EchoServer_{}_{}'.format(*self.address)
        )
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('sent {!r}'.format(data))

    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

# Make a server
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

# In to ETERNAL LOOP for handling all connections
try:
    event_loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()
'''

#24 asyncio echo client protocol

import asyncio
import functools
import logging
import sys

'''
MESSAGES = [
        b'This is the message. ',
        b'It will be sent ',
        b'in parts.',
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()


class EchoClient(asyncio.Protocol):

    def __init__(self, message, future):
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
                'connecting to {} port {}'.format(*self.address)
        )
        # transport.writelines() not good this
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('sending {!r}'.format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))

    def eof_received(self):
        self.log.debug('received EOF')
        self.transport.close()

        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed connection')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection.lost(exc)

client_completed = asyncio.Future()

client_factory = functools.partial(
        EchoClient,
        messages=MESSAGES,
        future=client_completed,
)
factory_coroutine = event_loop.create_connection(
        client_factory,
        *SERVER_ADDRESS,
)

log.debug('waiting for client to complete')
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
finally:
    log.debug('closing event loop')
    event_loop.close()

EXPECTED RESULTS:
asyncio: Using selector: KqueueSelector
main: waiting for client to comlete
EchoClient: connecting to ::1 port 1000
EchoClient: sending b'This is the message. '
EchoClient: sending b'It will be sent '
EchoClient: sending b'in parts.'
EchoClient: received b'This is the message. It will be sent in parts.'
EchoClient: received EOF
EchoClient: server closed connection
main: closing event loop
'''

#25 asyncio echo server coroutine

import asyncio
import logging
import sys

'''
SERVER_ADDRESS = ('localhost', 10000)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')

    while True:
        data = await reader.read(128)

        if data:
            log.debug('received {!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('sent {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return

# Make a server
factory = asyncio.start_server(echo, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()

RESULTS:
<stdin>:1210: DeprecationWarning: There is no current event loop
asyncio: Using selector: EpollSelector
main: starting up on localhost port 10000
^Cmain: closing server
main: closing event loop
'''

#26 asyncio echo client coroutine

import asyncio
import logging
import sys

'''
MESSAGES = [
        b'This is the message. ',
        b'It will be sent ',
        b'in parts.',
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

async def echo_client(address, messages):

    log = logging.getLogger('echo_client')

    log.debug('connecting to {} port {}'.format(*address))
    reader, writer = await asyncio.open_connection(*address)
    # transport.writelines() not good for this situation
    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    if writer.can_write_eof():
        writer.write_eof()
    await writer.drain()

    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return

    try:
        event_loop.run_until_complete(
            echo_client(SERVER_ADDRESS, MESSAGES)
        )
    finally:
        log.debug('closing event loop')
        event_loop.close()

RESULTS:
<stdin>:1275: DeprecationWarning: There is no current event loop
asyncio: Using selector: EpollSelector
'''

#27 SSL for client/server code above

# for server
# first:
# $ openssl req -newkey rsa:2048 -nodes -keyout pymotw.kew -x509 -days 365 -out pymotw.crt

# then change:
# factory = asyncio.start_server(echo, *SERVER_ADDRESS)
# server = event_loop.run_until_complete(factory)

# Make sertificate with hostname pymotw.com, if other host code not correct
# Then host checket in False
'''
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = Fasle
ssl_context.load_cert_chain('pymotw.crt', 'pymotw.key')

# Make server
factory = asyncio.start_server(echo, *SERVER_ADDRESS, ssl=ssl_context)

# And the change code for client
# then where:
# reader, writer = await asyncio.open_connection(*address)

ssl_context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
)
ssl_context.check_hostname = False
ssl_context.load_verify_location('pymotw.crt')
reader, writer = await asyncio.open_connection(
        *server_address, ssl=ssl_context)

# Change work with eof to work with NULL

#for msg in messages:
#    writer.write(msg)
#    log.debug('sending {!r}'.format(msg))
#if writer.can_write_eof():
#    writer.write_eof()
#await writer.drain()

# to:
for msg in messages:
    write.write(msg)
    log.debug('sending {!r}'.format(msg))
# SSL not work with EOF then for mark end of message use (b'\x00')
writer.write(b'\x00')
await writer.drain()

# for client:

async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')
    while True:
        data = await reader.read(128)
        terminate = dat.endswith(b'\x00')
        data = data.rstrip(b'\x00')
        if data:
            log.debug('received{!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('sent {!r}'.format(data))
        if not data or terminate:
            log.debug('message terminated, closing connection')
            writer.close()
            return

'''

#28 asyncio getaddrinfo

import asyncio
import logging
import socket
import sys

'''
TARGETS = [
        ('pymotw.com', 'https'),
        ('petricpetrushka.com', 'https'),
        ('python.org', 'https'),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,
        )

        for host in info:
            print('{:20}: {}'.format(target[0], host[4][0]))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()

EXPECTED RESULTS:
pymotw.com         : 66.33.211.242
...
'''
#29 asincio get name info

import asyncio
import logging
import socket
import sys

'''
TARGETS = [
        ('66.33.211.242', 443),
        ('104.130.43.121', 443),
]


async def  main(loop, targets):
    for target in targets:
        info = await loop.getnameinfo(target)
        print('{:15}: {} {}'.format(target[0], *info))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()

EXPECTED RESULTS:
66.33.211.242  : apache2-echo.catalina.dreamhost.com https
104.130.43.121 : 104.130.43.121 https

'''

#30 asyncio subprocess protocol

import asyncio
import functools

'''
async def run_df(loop):
    print('in run_df')

    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(
            factory,
            'df', '-h1',
            stdin=None,
            sterr=None,
    )
    try:
        print('launching process')
        transport, protocol = await proc
        print('waiting for process to completer')
        await cmd_done
    finally:
        transport.close()

    return cmd_done.result()


class DFProtocol(asyncio.SubprocessProtocol):

    FD_NAMES = ['stdin', 'stdout', 'stderr']

    def __init__(self, done_future):
        self.done = done_future
        self.buffer = bytearray()
        super().__init__()

    def connection_made(self, transport):
        print('process started {}'.format(transport.get_pid()))
        self.transport = transport

    def pipe_data_received(self, fd, data):
        print('read {} bytes from {}'.format(len(data),
            self.FD_NAMES[fd]))
        if fd == 1:
            self.buffer.extend(data)

    def process_exited(self):
        print('process exited')
        return_code = self.transport.get_returncode()
        print('return code {}'.format(return_code))
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            retults = self._parse_results(cmd_output)
        else:
            results = []
        self.done.set_results((return_code, results))

    def _parse_results(self, output):
        print('parsing results')
        if not output:
            return[]
        lines = output.split.splitlines()
        headers = lines[0].split()
        devices = lines[1:]
        retults = [
                dict(zip(headers, line.split()))
                for line in devices
        ]
        return results

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
            run_df(event_loop)
    )
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('\nFree space:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))

EXPECTED RESULTS:
in run_df
launching process
process started 49675
waiting for process to complete
read 332 bytes from stdout
process exited
return code 0
parsing results

Free space:

/                          : 233Gi
/Volumes/hobointernal      : 157Gi
/Volumes/hobo-tm           : 2.3Ti
'''

#32 asyncio subprocess coroutine

import asyncio
import asyncio.subprocess

'''
async def run_df():
    print('in run_df')

    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
            'df', '-h1',
            stdout=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print('process started {}'.format(proc.pid))

    while True:
        line = await proc.stdout.readline()  # or read()
        print('read {!r}'.format(line))
        if not line:
            print('no more output from command')
            break
        buffer.extend(line)

    print('waiting for process to complete')
    await proc.wait()

    return_code = proc.returncode
    print('return code {}'.format(return_code))
    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    else:
        results = []
    return (return_code, results)

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
            run_df()
    )
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('\nFree space:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))

RESULTS:
<stdin>:1595: DeprecationWarning: There is no current event loop
in run_df
launching process
process started 482377
df: invalid option -- '1'
Try 'df --help' for more information.
read b''
no more output from command
waiting for process to complete
return code 1
error exit 1
'''

#33 asyncio subprocess coroutine write

import asyncio
import asyncio.subprocess

'''
async def to_upper(input):
    print('in to_upper')

    create = asyncio.create_subprocess_exec(
            'tr', '[:lower:]', '[:upper:]',
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print('pid {}'.format(proc.pid))

    print('communicating with process')
    stdout, stderr = await proc.communicate(input.encode())

    print('waiting for process to complete')
    await proc.wait()

    return_code = proc.returncode
    print('return code {}'.format(return_code))
    if not return_code:
        results = bytes(stdout).decode()
    else:
        results = ''

    return (return_code, results)

MESSAGE = """
This message will be converted
to all caps.
"""

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
            to_upper(MESSAGE)
    )
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('Original: {!r}'.format(MESSAGE))
    print('Changed : {!r}'.format(results))

RESULTS:
<stdin>:1662: DeprecationWarning: There is no current event loop
in to_upper
launching process
pid 483185
communicating with process
waiting for process to complete
return code 0
Original: '\nThis message will be converted\nto all caps.\n'
Changed : '\nTHIS MESSAGE WILL BE CONVERTED\nTO ALL CAPS.\n'
'''

#34 asyncio signal

import asyncio
import functools
import os
import signal

'''
def signal_handler(name):
    print('signal_handler({!r})'.format(name))

event_loop = asyncio.get_event_loop()

event_loop.add_signal_handler(
        signal.SIGHUP,
        functools.partial(signal_handler, name='SIGHUP'),
)
event_loop.add_signal_handler(
        signal.SIGUSR1,
        functools.partial(signal_handler, name='SIGUSR1'),
)
event_loop.add_signal_handler(
        signal.SIGINT,
        functools.partial(signal_handler, name='SIGING'),
)

async def send_signals():
    pid = os.getpid()
    print('starting send_signals for {}'.format(pid))

    for name in ['SIGHUP', 'SIGHUP', 'SIGUSR1', 'SIGINT']:
        print('sending {}'.format(name))
        os.kill(pid, getattr(signal, name))
        # get step up for handler of signals
        print('yielding control')
        await asyncio.sleep(0.01)
    return

try:
    event_loop.run_until_complete(send_signals())
finally:
    event_loop.close()

RESULTS:
<stdin>:1699: DeprecationWarning: There is no current event loop
starting send_signals for 484793
sending SIGHUP
yielding control
signal_handler('SIGHUP')
sending SIGHUP
yielding control
signal_handler('SIGHUP')
sending SIGUSR1
yielding control
signal_handler('SIGUSR1')
sending SIGINT
yielding control
signal_handler('SIGING')
'''

#35 asyncio executor thread for not adapted for asyncio programms

import asyncio
import concurrent.futures
import logging
import sys
import time

'''
def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
            loop.run_in_executor(executor, blocks, i)
            for i in range(6)
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    logging.basicConfig(
            level=logging.INFO,
            format='%(threadName)10s %(name)18s: %(message)s',
            stream=sys.stderr,
    )

    # make pull of threads
    executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
                run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()

RESULTS:
<stdin>:1795: DeprecationWarning: There is no current event loop
MainThread run_blocking_tasks: starting
MainThread run_blocking_tasks: creating executor tasks
ThreadPoolExecutor-0_0          blocks(0): running
ThreadPoolExecutor-0_1          blocks(1): running
ThreadPoolExecutor-0_2          blocks(2): running
MainThread run_blocking_tasks: waiting for executor tasks
ThreadPoolExecutor-0_0          blocks(0): done
ThreadPoolExecutor-0_1          blocks(1): done
ThreadPoolExecutor-0_0          blocks(3): running
ThreadPoolExecutor-0_1          blocks(4): running
ThreadPoolExecutor-0_2          blocks(2): done
ThreadPoolExecutor-0_2          blocks(5): running
ThreadPoolExecutor-0_0          blocks(3): done
ThreadPoolExecutor-0_1          blocks(4): done
ThreadPoolExecutor-0_2          blocks(5): done
MainThread run_blocking_tasks: results: [4, 25, 9, 1, 0, 16]
MainThread run_blocking_tasks: exiting
'''

#36 asyncio executor process for every core of CPU

# Change the previous code
'''
if __name__ == '__main__':
    logging.basicConfig(
            level_logging.INFO,
            format='PID %(process)5s %(name)18s: %(message)s',
            stream=sys.stderr,
    )

    executor = concurrent.futures.ProcessPoolExecutor(
            max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
                run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()

EXPECTED RESULTS:
PID 16429 run_blocking_tasks: starting
                            : creating executor tasks
                            : waiting for executor tasks
PID 16430 blocks(0): running
       31       (1): running
       32       (2): running
       30 blocks(0): done
       32 blocks(2): done
       31 blocks(1): done
       30 blocks(3): running
       32       (4): running
       31       (5): running
       31 blocks(5): done
       32 blocks(4): done
       30 blocks(3): done
PID 16429 run_blocking_tasks: results: [4, 0, 16, 1, 9, 25]
PID 16429 run_blocking_tasks: exiting
'''

#37 asyncio debug
