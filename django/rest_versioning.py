"""Django REST versioning about."""


#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': (
            'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        ),
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '3/hour',
            'user': '10/hour',
            'drones': '20/hour',
            'pilots': '15/hour',
        },
        'DEFAULT_VERSIONING_CLASS': (
            'rest_framework.versioning.NamespaceVersioning',
        ),
}

