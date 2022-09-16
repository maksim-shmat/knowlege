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

#5 contextmanager() as decorator
