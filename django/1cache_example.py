""" Cached session backend. """

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Caching frameworks
django-cache-machine
django-cachalot

# the following router would direct all cache read operations to cache_replica,
# and all write operations to cache_primary.
class CacheRouter:
    """A router to control all database cache operations"""

    def db_read(self, model, **hints):
        "All cache read operations go to the replica"
        if model._meta.app_label == 'django_cache':
            return 'cache_replica'
        return None

    def db_for_write(self, model, **hints):
        "All cache write operations go to primary"
        if model._meta.app_label == 'django_cache':
            return 'cache_primary'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        "Only install the cache model on primary"
        if app_label == 'django_cache':
            return db == 'cache_primary'
        return None
########
# automatically cache the view's response
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):

##########
# use key_prefix and special_cache
@cache_page(60 * 15, cache="special_cache")
def my_view(request):
    ...

@cache_page(60 * 15, key_prefix="site1")
def my_view(request):
    ...

###########
# specifying per-view cache in the URLconf
from django.views.decorators.cache import cache_page

urlpatterns = [
        path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
##########

