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

######### define log messages in a Python module
# Python logging package
import logging

# Standard instance of a logger with __name__
stdlogger = loggig.getLogger(__name__)

# Custom instance logging with explicit name
dbalogger = logging.getLogger('dba')

def index(request):
    stdlogger.debug("Entering index method")

def contactform(request):
    stdlogger.info("Call to contactform method")

    try:
        stdlogger.debug("Entering store_id conditional block")
        # Logic to handle store_id
    except Exception, e:
        stdlogger.exception(e)

    stdlogger.info("Starting search on DB")
    try:
        stdlogger.info("About to search db")
        # Loging to search db
    except Exception, e:
        stdlogger.error("Error in searchdb method")
        dbalogger.error("Error in searchdb method, stack %s" % (e))

##########
