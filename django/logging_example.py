""" It is more add to LOGGING from settings.py. """

# views.py
import logging
logger = logging.get Logger(__name__)

def complicated_view():
    logger.debug("Entered the complicated_view()!")
