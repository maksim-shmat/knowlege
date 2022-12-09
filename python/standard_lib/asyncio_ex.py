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
