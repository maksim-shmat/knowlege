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
