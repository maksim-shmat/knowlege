"""Contextlib about."""

#1 contextlib api

class Context:
    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')

with Context():
    print('Doing work in the context')

'''RESULTS:
__init__()
__enter__()
Doing work in the context
__exit__()
'''

#2 return other object

class WithinContext:

    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))

    def do_something(self):
        print('WithinContext.do_something()')

    def __del__(self):
        print('WithinContext.__del__')


class Context:

    def __init__(self):
        print('Context.__init__()')

    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')

with Context() as c:
    c.do_something()

'''RESULTS:
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x7f412f4dffd0>)
WithinContext.do_something()
Context.__exit__()
WithinContext.__del__
'''

#3 contextlib decorator

import contextlib

class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))

    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))

@Context('as decorator')
def func(message):
    print(message)
print()
with Context('as context manager'):
    print('Doing work in the context')
print()
func('Doing work in the wrapped function')

'''RESULTS:
__init__(as decorator)

__init__(as context manager)
__enter__(as context manager)
Doing work in the context
__exit__(as context manager)

__enter__(as decorator)
Doing work in the wrapped function
__exit__(as decorator)
WithinContext.__del__
'''

#4 contexmanager

import contextlib

@contextlib.contextmanager
def make_context():
    print(' entering')
    try:
        yield {}
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')

print('Normal:')
with make_context() as value:
    print(' inside with statement:', value)
'''
print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')
'''
'''RESULTS:
Normal:
 entering
 inside with statement: {}
  exiting

Handled error:
 entering
  ERROR: showing example of handling an error
  exiting

Unhandled error:
 entering
  exiting
Traceback (most recent call last):
  File "<stdin>", line 128, in <module>
ValueError: this exception is not handled
WithinContext.__del__

shell returned 1
'''

#5 contextlib ignore error

import contextlib

class NonFatalError(Exception):
    pass

def non_idempotent_operation():
    raise NonFatalError(
            'The operation failed because of existing state'
    )

try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
except NonFatalError:
    pass

print('done')

#5 contextlib.suppress() against try/except

import contextlib

class NonFatalError(Exception):
    pass

def non_idempotent_operation():
    raise NonFatalError(
            'The operation failed'
    )
with contextlib.suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
print('done')

'''RESULTS: (For both #5)
trying non-idempotent operation
done
trying non-idempotent operation
done
'''

#6 redirect

from contextlib import redirect_stdout, redirect_stderr # it's danger for safe
import io
import sys

def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))

capture = io.StringIO()
with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())

'''RESULTS:
(stdout) A: 5
(stderr) A: 5
'''

#7 exitstack enter context

import contextlib

@contextlib.contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield {}
    print('{} exiting'.format(i))

def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)

variable_stack(2, 'inside context')

'''RESULTS:
0 entering
1 entering
inside context
1 exiting
0 exiting
'''

#8 Handling errors for chunk of code

import contextlib

class Tracker:
    """Base Class fro context manager how generate errors."""
    
    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('s  {}({}): {}'.format(
            self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    """If get exception, count it handled."""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(
                exc_details[1]))
        self.msg('exiting {}'.format(received_exc))
        # Return bulean for handle exception
        return received_exc


class PassError(Tracker):
    """If get exception, move it farther."""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(
                exc_details[1]))
        self.msg('exiting')
        # return False if exception not handled
        return False


class ErrorOnExit(Tracker):
    """Generate exception."""

    def __exit__(self, *exc_details):
        self.msg('throwing error')
        raise RuntimeError('from {}'.format(self.i))


class ErrorOnEnter(Tracker):
    """Generate exception."""

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('exiting')

#9 exitstack() callback()
