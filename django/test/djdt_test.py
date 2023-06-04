"""DjDT third party test case named django-debug-toolbar, about it."""

#1 pip install django-debug-toolbar
ad it to requirements.tst

#2 settings.py

INSTALLED_APPS = [
        ...
        'django.contrib.staticfiles',
        'debug_toolbar',
        ...
]

MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        ...
]

INTERNAL_IPS = [
        '127.0.0.1',
]

STATIC_URL = 'staticfiles/'

def show_toolbar(request):
    return True

if os.getenv('SHOW_TOOLBAR_CALLBACK') == 'True':
    DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

#3 urls.py

from django.urls import ..., include, re_path
...
if settings.DEBUG:
    ...
    import debug_toolbar

    urlpatterns = [
            re_path(
                r'^__debug__/',
                include(debug_toolbar.urls)
            ),
    ] + urlpatterns

#4 if use .env then:
SHOW_TOOLBAR_CALLBACK=True

#5 logging
# views.py

import logging

def practice_year_view(request, year):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.info('The Requested Year Is: %s' % year)
    ...
