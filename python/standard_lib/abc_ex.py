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

#5 
