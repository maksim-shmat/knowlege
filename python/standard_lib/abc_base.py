""" Base file for others in theme abstract."""

import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Get data from input chanel
        and return object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save object of data for out."""
