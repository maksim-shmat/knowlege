""" It is more add to LOGGING from settings.py. """

# views.py
import logging
logger = logging.get Logger(__name__)

def complicated_view():
    logger.debug("Entered the complicated_view()!")

########## define loggers in a Python module
# Python logging package
import logging

# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

# Custom instance logging with explicit name
dbalogger = logging.getLogger('dba')

#########
