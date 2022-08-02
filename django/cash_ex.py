"""Cashing about."""

#1
from django.views.docorators.cache import cache_page

@cache_page(24 * 60 * 60)
def top_stories_yesterday(request):
    # ... get stories and return HttpResponse

@cache_page(5 * 60)  
def top_stories_today(request):
    # ... get stories an return HttpResponse
    
#2 for never cache one page

from django.views.decorators.cache import  never_cache

@never_cache
def top_stories_this_second(request):
    # not chach this page

#3 Revalidate from other servers

from django.views.decorators.cache import cache_control

@cache_control(must_revalidate=True)
def revalidate_me(request):
    # ...

#4 If for one URL need different content e.g. other language

from django.views.decorators.vary import vary_on_headers

@vary_on_headers("Accept-Language")
def localized_view(request):
    # ...

#5 line for line it's too long for big data, add cache

def stats_from_log(request, stat_name):
    logfile = file("/var/log/imaginary.log")
    stat_list = [line for line in logfile if line.startswith(stat_name)]
    # not good for big files

# add cache

from django.core.cache import cache

def stats_from_log(request, stat_name):
    stat_list = cache.get(stat_name)  # return object from cache 
                                      # if time not ower, else return None
    if stat_list == None:
        logfile = file("/var/log/imaginary.log")
        stat_list = [line for line in logfile if line.startswith(stat_name)]
        cache.set(stat_name, stat_list, 60)  # 60 sec or time from CACHE_BACKEND

#6 cash chunk in template example

{% load cache %}
... Other not cashed chunks of page
{% cache 300 list_of_stuff %}
  {% for item in really_long_list_of_items %}
    {{ item.do_expensive_rendering_step }}
  {% endfor %}
{% endcache %}
... Another not cached chunks from page

#7 CACHE_BACKEND example

CACHE_BACKEND = "locmem://?max_entries=1000&cull_percentage=4&timeout=60"
# it's localmemory, 1000 notes limit, if cache ower del 1/4, 60 sec for cache.

CACHE_BACKEND = "file:///var/chache/django/mysite"  # for cache to file

$ python manage.py createcachetable cache  # create table in db
CACHE_BACKEND = "db://cache/"  # table with 3 column: cache_key, value, expires(datetime)

$ memcached -d -m 2048 -l 10.0.1.1  # start demon, get 2Gb, get quiree from IP10.0.1.1
CACHE_BACKEND = "memcached://10.0.1.1:11211"  # default port for memcached 11211
CACHE_BACKEND = "memcached://10.0.1.1:11211;10.0.5.5:11211"  # ; for both servers
