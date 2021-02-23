""" Example of settings."""

# Default PostgreSQL and MySQL called users
DATABASES = {
        'default': {
            'NAME': 'app_data',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'postgres_user',
            'PASSWORD': 's3krit'
        },
        'users': {
            'NAME': 'user_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_user',
            'PASSWORD': 'priv4te'
        }
}

###############
# default free ant set up DATABASE_ROUTERS
DATABASES = {
        'default': {},
        'users': {
            'NAME': 'user_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_user',
            'PASSWORD': 'superS3cret'
        },
        'customers': {
            'NAME': 'customer_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_cust',
            'PASSWORD': 'veryPriv@te'
        }
}

#############
# configuring logging
# settings.py
import os

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
                'propagate': False,
            },
        },
}

### settings.py
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/path/to/django/debug.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
}

### settings.py
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} { thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'filters': {
            'special': {
                '()': 'project.logging.SpecialFilter',
                'foo': 'bar',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['special']
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'myproject.custom': {
                'handlers': ['console', 'mail_admin'],
                'level': 'INFO',
                'filters': ['special']
            }
        }

}

########## disables Django's logging configuration and then manually configures logging
# settings.py
LOGGING_CONFIG = None

import logging.config
logging.config.dictConfig(...)

##### languages
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
        ('de', _('German')),
        ('en', _('English')),
]

######### django settings.py with absolute path values
# Other configuration variables omitted for brevity
STATIC_ROOT = '/www/STORE/coffeestatic/'

# Other configuration variables omitted for brevity
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['/www/STORE/coffeehouse/templates/',],
}
]

######### django settings.py with dynamically determined absolute path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Other configuration variables omitted for brevity
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['%s/templates/'% (PROJECT_DIR),],
}
]

######### django settings.py with control variable with host name to load# different sets of variables
# Import socket to read host name
import socket

# If the host name starts with 'live', DJANGO_HOST = "production"
if socket.gethostname().startswith('live'):
    DJANGO_HOST = "production"

# Else if host name starts with 'test', set DJANGO_HOST = "test"
elif socket.gethostname().startswith('test'):
    DJANGO_HOST = "testing"
else:
# If host doesn't match, assume it's a development server, set DJANGO_HOST = "development"
    DJANGO_HOST = "development"

    # Define general behavior variables for DJANGO_HOST and all others
    if DJANGO_HOST == "production":
        DEBUG = False
        STATIC_URL = '/static/
        '
# Define DATABASES variable for DJANGO_HOST and all others
if DJANGO_HOST == "production":
    # Use mysql for live host
    DATABASES = {
            'default': {
                'NAME': 'housecoffee',
                'ENGINE': 'django.db.backends.mysql',
                'USER': 'coffee',
                'PASSWORD': 'secretpass'
            }
    }
else:
    # Use sqlite for non live host
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'coffee.sqlite3'),
            }
        }

# Define EMAIL_BACKEND variable for DJANGO_HOST
if DJANGO_HOST == "production":
    # Output to SMTP server on DJANGO_HOST production
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
elif DJANGO_HOST == "testing":
    # Nullify output on DJANGO_HOST test
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Define CACHES variable for DJANGO_HOST production and all other hosts
if DJANGO_HOST == 'production':
    # Set cache
    CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                'LOCATION': '127.0.0.1:11211',
                'TIMEOUT': '1800',
                }
            }
    CACHE_MIDDLEWARE_SECONDS = 1800
    
else:
    # No cache for all other hosts
    pass
