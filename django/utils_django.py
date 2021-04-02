""" About utils django."""

###### cached_property(func)

class Foo(object):
    @property
    def bar(self):
        parint('Called the method!')
        return 'baz'

f = Foo()
f.bar
# Called the method!
# 'baz'
f.bar
# Called th method!
# 'baz'

### 
from django.utils.functional import cached_property

class Foo(object):
    @cached_property
    def bar(self):
        print('Called the method!')
        return 'baz'

f = Foo()
f.bar
# Called the method!
# 'baz'
f.bar
'baz'

###### curry(func)

from django.utils.functional import curry

def normalize_value(value, max_value, factor=1, comment='Original'):
    """
    Normalizes the given value according to the provided maximum,
    scaling it according to factor.
    """
    return '%s (%s)' % (float(value) / max_value * factor, comment)
noralize_value(3, 4)
# '0.75 (Original)'
normalize_value(3, 4, factor=2, comment='Double')
# '1.5 (Double)'
percent = curry(normalize_value, max_value=100, comment='Percent')
percent(50)
# '0.5 (Percent)'
percent(50, factor=2, comment='Double')
# '1.0 (Double)'
tripled = curry(normalize_value, factor=3, comment='Triple')
tripled(3, 4)
# '2.25 (Triple)'

###### Breack indempotency with memoize() from django

from django.utils.functional import memoize
def median(value_list):
    """
    Finds the median value of a list of numbers
    """
    print 'Executing the function!'
    value_list = sorted(value_list)
    half = int(len(value_list) / 2)
    if len(value_list) % 2:
        # Odd number of values
        return value_list[half]
    else:
        # Even number of values
        a, b = value_list[half - 1:half + 1]
        return float(a + b) / 2
primes = (2, 3, 5, 7, 11, 13, 17)
fibonacci = ( 0, 1, 1, 2, 3, 5, 8, 13)
median(primes)
# Executing the function!
# 7
median(primes)
# Executing the function!
# 7
median = memoize(median, {}, 1)
median(primes)
# Executing the function!
# 7
median(primes)
# 7
median(fibonacci)
# Executing the function!
# 2.5
median(fibonacci)
# 2.5

###### partition(predicate, values)

from django.utils.functionl import prtition

prtition(lambda x: x > 4, range(10))
([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])

# 
even, odd = partition(lambda x: x % 2, range(10))
even
# [0, 2, 4, 6, 8]
odd
[1, 3, 5, 7, 9]

######
