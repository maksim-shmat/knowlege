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

#5
