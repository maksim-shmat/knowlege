""" for abc_base.py."""

#1

import abc

from abc_base import PluginBase

'''
class LocalBaseClass:
    pass


@PluginBase.register
class RegisteredImplementation(LocalBaseClass):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation,
                                  PluginBase))

    print('Instance:', isinstance(RegisteredImplementation(),
                                  PluginBase))

RESULTS:
Subclass: True
Instance: True
'''

#2

"""for abc_base.py."""

import abc

from abc_base import PluginBase

'''
class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(SubclassImplementation,
                                  PluginBase))
    print('Instance:', isinstance(SubclassImplementation(),
                                  PluginBase))

RESULTS:
Subclass: True
Instance: True
'''

#3 abc find subclasses

import abc
'''
from abc_base import PluginBase
import abc_subclass
import abc_register


for sc in PluginBase.__subclass__():
    print(sc.__name__)

'''

#4 abc concrete method

import abc
import io

'''
class ABCWithConcreteImplementation(abc.ABC):

    @abc.abstractmethod
    def retrieve_values(self, input):
        print('base class reading data')
        return input.read()


class ConcreteOverride(ABCWithConcreteImplementation):

    def retrieve_values(self, input):
        base_data = super(ConcreteOverride,
                self).retrieve_values(input)
        print('subclass sorting data')
        response = sorted(base_data.splitlines())
        return response

input = io.StringIO("""line one
line two
line three
""")

reader = ConcreteOverride()
print(reader.retrieve_values(input))
print()

RESULTS:
base class reading data
subclass sorting data
['line one', 'line three', 'line two']
'''

#5 abc abstractproperty

import abc

'''
class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Should never reach here'

    @property
    @abc.abstractmethod
    def constant(self):
        return 'Should never reach here'

class Implementation(Base):

    @property
    def value(self):
        return 'concrete property'

    constant = 'set by a class attribute'


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value    :', i.value)
print('Implementation.constant :', i.constant)

RESULTS:
ERROR: Can't instantiate abstract class Base with abstract methods constant, value
Implementation.value    : concrete property
Implementation.constant : set by a class attribute
'''

#6 abc abstractproperty rw

import abc

'''
class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Should never reach here'

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        return


class PartialImplementation(Base):

    @property
    def value(self):
        return 'Read-only'


class Implementation(Base):

    _value = 'Default value'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

p = PartialImplementation()
print('PartialImplementation.value:', p.value)

try:
    p.value = 'Alteration'
    print('PartialImplementation.value:', p.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value:', i.value)

i.value = 'New value'
print('Changed value:', i.value)

RESULTS:
ERROR: Can't instantiate abstract class Base with abstract method value
PartialImplementation.value: Read-only
ERROR: can't set attribute 'value'
Implementation.value: Default value
Changed value: New value
'''

#7 abc class static

import abc

'''
class Base(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def factory(cls, *args):
        return cls()

    @staticmethod
    @abc.abstractmethod
    def const_behavior():
        return 'Should never reach here'


class Implementation(Base):

    def do_something(self):
        pass

    @classmethod
    def factory(cls, *args):
        obj = cls(*args)
        obj.do_something()
        return obj

    @staticmethod
    def const_behavior():
        return 'Static behavior differs'


try:
    o = Base.factory()
    print('Base.value:', o.const_behavior())
except Exception as err:
    print('ERROR:', str(err))

i = Implementation.factory()
print('Implementation.const_behavior :', i.const_behavior())

RESULTS:
ERROR: Can't instantiate abstract class Base with abstract methods const_behavior, factory
Implementation.const_behavior : Static behavior differs
'''
