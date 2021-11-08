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

######4 
