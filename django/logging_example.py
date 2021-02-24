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

########## custom LOGGING Django configuration
LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d]%(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'development_logfile': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.FileHandler',
                'filename': '/tmp/django_dev.log',
                'formatter': 'verbose'
            },
            'production_logfile': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/django/django_production.log',
                'maxBytes': 1024*1024*100, # 100MB
                'backupCount': 5,
                'formatter': 'simple'
            },
            'dba_logfile': {
                'level': 'DEBUG',
                'filters': ['require_debug_false', 'require_debug_true'],
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': '/var/log/dba/django_dba.log',
                'formatter': 'simple'
            },
        },
        'rooot': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        'loggers': {
                'coffeehouse': {
                    'handlers': ['development_logfile','production_logfile'],
                },
                'dba': {
                    'handlers': ['dba_logfile'],
                },
                'django': {
                    'handlers': ['development_logfile','production_logfile'],
                },
                'py.warnings': {
                    'handlers': ['development_logfile'],
                },
            }
    }

############ django project configuration to communicate with Sentry via Raven
INSALLED_APPS = [
        ...
        'raven.contrib.django.raven_compat',
        ...
]

RAVEN_CONFIG = {
        'dsn': '<your_dsn_value>@sentry.io/<your_dsn_value>',
}

########### django logging handler for Sentry/Raven
LOGGING = {
        ...
        'handlers': {
            ...
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.handlers.SentryHandler',
            },
            ...
    }

###########
