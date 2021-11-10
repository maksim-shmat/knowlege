"""Logging about."""

######1 Import logging Library

import logging

logging.warning("This is a simple Python logging example")

######2 Logging messages to log file

logging.basicConfig(filename="jill.log")

logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
logging.critical('This is a CRITICAL message')

######3 Logging messages to log file using handler

import logging

# create a logger
logger = logging.getLogger('mylogger')

handler = logging.FileHandler('jill.log')
logger.addHandler(handler)

logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CRITICAL message')

######4 Log DEBUG lines

import logging

# create a logger
logger = logging.getLogger('mylogger')
# set logging level
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('jill.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# write a debug message
logger.debug('This is a DEBUG message')

######5 Log only DEBUG lines using Python logger

import logging

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

# create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('jill.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# set filter to log only DEBUG lines
handler.addFilter(MyFilter(logging.DEBUG))
logger.addHandler(handler)

# write a debug line to log file
logger.debug('This is a DEBUG message')
logger.info('This is a INFO message')
logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CRITICAL message')

######6
