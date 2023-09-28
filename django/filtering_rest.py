"""Filetering with Django RESTful, about."""

#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'drones.custompagination.LimitOffsetPaginationWithBound',
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
}

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Django REST Framework
        'rest_framework',
        # Drones application
        'drones.apps.DronesConfig',
        # Django Filters,
        'django_filters',
]

#2
