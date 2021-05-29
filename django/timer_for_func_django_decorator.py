""" Check time for func django with decorator."""

# make decorator
def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            t0 = time.time()
            return func(*args, **kwargs)
        finally:
            t1 = time.time()
            writeto(
                    'View Function',
                    '({})'.format(prefix) if prefix else '',
                    func.__name__,
                    args[1:],
                    'Took',
                    '{:.2f}ms'.format(1000 * (t1 - t0)),
                    args[0].build_absolute_uri(),
            )
    return inner
return decorator

### use it decorator
from wherever import view_function_timer

@view_function_timer()
def homepage(request, thing):
    ...
    return render(request, template, context)
