"""Abstract type examples."""

class BaseQueue(object):
    """Abstract/Virtual Class."""
    def __init__(self):
        self.contents = list()
        raise NotImplementedError

    def Enqueue(self, item):
        raise NotImplementedError

    def Dequeue(self):
        raise NotImplementedError

    def Print_Contents(self):
        for i in self.contents:
            print(i,)

# Abstract type with the standard abc module

from abc import ABCMeta, abstractmethod

class BaseQueue():
    """Abstract Class."""
    __metaclass__ = ABCMeta

    def __init__(self):
        self.contents = list()

    @abstractmethod
    def Enqueue(self, item):
        pass

    @abstractmethod
    def Dequeue(self):
        pass

    def Print_Contents(self):
        for i in self.contents:
            print(i,)
