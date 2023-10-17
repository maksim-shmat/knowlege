"""Throttling Django REST about."""

#1 settings.py

REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
        'drones.custompagination.LimitOffsetPaginationWithUpperBound',
        'PAGE_SIZE': 4,
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.OrderingFilter',
            'rest_framework.filters.SearchFilter',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '3/hour',
            'user': '10/hour',
            'drones': '20/hour',
            'pilots': '15/hour',
        }
}
        
