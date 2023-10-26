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

######## python configparser sample file production.cfg
[general]
DEBUG: false
STATIC_URL: http://static.coffeehouse.com/

[databases]
NAME: housecoffee
ENGINE: django.db.backends.mysql
USER: coffee
PASSWORD: secretpass

[securirty]
SECRET_KEY: %%ea)cjy@v9(7!b(20gl+4-6iur28dyb=tciuou00ye9wr

######### django settings.py with configparser import
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Access configparser to load variable values
from django.utils.six.moves import configparser
config = configparser.SafeConfigParser(allow_no_value=True)

# Import socket to read host name
import socket

# If the host name starts with 'live', load configparser from "production.cfg"
if socket.gethostname().startswith('live'):
    config.read('%s/production.cfg' % (PROJECT_DIR))

# Else if host name starts with 'test', load configparser from "testing.cfg"
elif socket.gethostname().startswith('test'):
    config.read('%s/testing.cfg' % (PROJECT_DIR))

else:
# If host doesn't match, assume it's a development server, load configparser from "development.cfg"
    config.read('%s/development.cfg' % (PROJECT_DIR))

DEBUG = config.get('general', 'DEBUG')
STATIC_URL = config.get('general', 'STATIC_URL')

DATABASES = {
    'default': {
        'NAME': config.get('databases', 'NAME'),
        'ENGINE': config.get('databases', 'ENGINE'),
        'USER': config.get('databases', 'USER'),
        'PASSWORD': config.get('databases', 'PASSWORD')
    }
}

SECRET_KEY = config.get('security', 'SECRET_KEY')

############ override DJANGO_SETTINGS_MODULE to load application variables
# from a file called testing.py and not the default settings.py
$ export DJANGO_SETTINGS_MODULE=coffeehouse.load_testing
$ python manage.py runserver
Validation models...

0 errors found
Django version 1.11, using settings 'coffeehouse.load_testing'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C
############ Django STATICFILES_DIR definition with namespaces in settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = ('%s/website-static-default/'% (BASE_DIR),
                   ('bootstrap', '%s/bootstrap-3.1.1-dist/'% (BASE_DIR)),
                   ('jquery', '%s/jquery-1-11-1-dist/'% (BASE_DIR)),
                   ('jquery-ui', '%s/jquery-ui-1.10.4/'% (BASE_DIR)),)

########### default LOGGING in Django projects
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequiredDebugTrue',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'null': {
                'class': 'logging.NullHandler',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'py.warnings': {
                'handlers': ['console'],
            },
        }
    }

########## django email conf for Gmail or Google Apps account
EMAIL_BACKENG='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='username@gmail.com/OR/username@coffeehouse.com'
EMAIL_HOST_PASSWORD='password'
EMAIL_USE_TLS=True

########### django email configuration for Amazon.com SES
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = '***************'
AWS_SECRET_ACCESS_KEY = '***********************'

########## django email configuration for SparkPost
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBacken'
EMAIL_HOST = 'smtp.sparkpostmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'SMTP_Injection'
EMAIL_HOST_PASSWORD = '<sparkpost_api_key>'
EMAIL_USE_TLS = True

######### Base Django allauth settings.py configuration

#Ensure th 'django.contrib.sites' is declared in INSTALLED_APPS
# And also add the allauth, allauth.account and allauth.socialaccount to INSTALLED_APPS

INSTALLED_APPS = [
        # Django sites app required
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
]

# Ensure SITE_ID is set sites app
SITE_ID = 1

# Add the 'allauth' backend to AUTHENTICATION_BACKEND and keep default ModelBackend AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend', allauth.account.auth_backends.AuthenticationBackend']

# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console
EMAIL_BACKEND='django.cor.mail.backends.console.EmailBackend'

# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

### Django allauth url configuration urls.py

urlpatterns = [
        ...
        url(r'^accounnts/', include('allauth.urls')),
        ...
]

###### DIRS definition with relative path in settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['%s/templates/' % (PROJECT_DIR),
                     '%S/dev_templates/' %(PROJECT_DIR),],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
]

#####

#1 Organizing templates

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
]

# urls.py
urlpatterns = [
        path'about/', TemplateView.as_view(template_name='about.html'),
        name='about'),
]
