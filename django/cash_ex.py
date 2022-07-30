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
