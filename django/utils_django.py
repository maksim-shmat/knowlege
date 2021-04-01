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

######
