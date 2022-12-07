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

#9
