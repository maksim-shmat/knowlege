"""Django settings about."""


#1 Build paths inside the project like this: os.path.join(BASE_DIR, ...)  realy?

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

#2 Good practice for different dirrectories

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['%s/templates/' % (PROJECT_DIR),],  # This
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

#3 Authentication classes in settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_ClASS':
        'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filter.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
            ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            )
}

#4 Django Rest Framework settings for secure API

REST_FRAMEWORK = {
        # Allow unauthenticated access to public content 
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ]
}

#4 Cached session backend

SESSION_ENGINE = "django.contrib.sessions.backend.cache"

#5
