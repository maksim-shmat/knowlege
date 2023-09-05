"""Logging about."""

######1 Import logging Library

import logging
logging.warning("This is a simple Python logging example")

######2 Logging messages to log file

logging.basicConfig(filename="jill.log")

logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
logging.critical('This is a CRITICAL message')
#2.1 logging file example

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.DEBUG,
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)

RESULTS:
FILE:
DEBUG:root:This message should go to the log file

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
# set logger level
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('jill.log')
# create a logging format
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

######6 Log INGO lines

import logging

# create a logger
logger = logging.getLogger('mylogger')
# set logger level
logger.setLevel(logging.INFO)
# or you can set the following level
# logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('jill.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# write a info message
logger.info('This is an INFO message')

######7 Log only INFO lines using Python logger

import logging

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

# create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('jill.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# set fileter to log only INFO lines
handler.addFilter(MyFilter(logging.INFO))
logger.addHandler(handler)

# write an INFO line to log file
logger.info('This is a INFO message')
logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CREITICAL message')

######8 Log WARNING lines

import logging

# create a logger
logger = logging.getLogger('mylogger')
# set logger level
logger.setLevel(logging.WARNING)
# or you can set one of the following level
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('jill.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
# write a Warning message
logger.warning('This is a WARNING message')

### Log only WARNING lines using python logger

import logging

class MyFiler(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

# create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler('jill.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# set filter to log only WARNING lines
handler.addFilter(MyFilter(logging.WARNING))
logger.addHandler(handler)

logger.warning('This is a WARNING message')
logger.error('This is an ERRRO message from WARNING work')
logger.critical('This is a CRITICAL message from WARNING work')

######9 Log ERROR lines

import logging

# create a logger
logger = logging.getLogger('mylogger')
# set logger level
logger.setLevel(logging.ERROR)
# or set one of the following level
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.INFO)
# loggetr.setLevel(logging.DEBUG)

handler = logging.FileHandler('jill.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(handler)

# write a error message
logger.error('This is an ERROR message')

### Log only ERROR lines using python logger

import logging

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

# create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('jill.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# set filter to log only ERROR lines
handler.addFilter(MyFilter(logging.ERROR))
logger.addHandler(handler)

logger.error('This is an ERROR message')
logger.critical('This is an CRITICAL message')
#10 

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("jill.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(levelname)s-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("This will get into the file!")

#11 

import logging

logging.basicConfig(level=logging.INFO, filename='jill.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1/0)
logging.info('The division succeeded')
logging.info('Ending program')

# 12 logging rotatingfile example

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# set logging level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add handler
handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME,
        maxBytes=20,
        backupCount=5,
)
my_logger.addHandler(handler)

# Write message to the logging journal
for i in range(20):
    my_logger.debug('i = %d' % i)

# Show list of created files
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)

RESULTS:
logging_rotatingfile_example.out.5
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
#13 logging level example

import logging
import sys

LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is an warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')

#14 logging modules example

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')

RESULTS:
WARNING:package1.module1:This message comes from one module
WARNING:package2.module2:This comes from another module

#15 logging captureWarnings()

import logging
import warnings

logging.basicConfig(
        level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warnig is sent to the logs')

RESULTS:
/home/jack/django2/knowlege/python/logging_ex.py:357: UserWarning: This warning is not sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:/home/jack/django2/knowlege/python/logging_ex.py:361: UserWarning: This warnig is sent to the logs
  warnings.warn('This warnig is sent to the logs')

#16 logging example

import logging

logging.basicConfig(
        filename='ch11.log',
        level=logging.DEBUG,  # minimum level capture in the file
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

mylist = [1, 2, 3]
logging.info('Starting to process 'mylist'...')

for position in range(4):
    try:
        logging.debug(
                'Value at position %s is %s', position, mylist[position]
        )
    except IndexError:
        logging.exception('Faulty position: %s', position)

logging.info('Done parsing `mylist`.')


