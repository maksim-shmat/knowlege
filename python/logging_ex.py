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
