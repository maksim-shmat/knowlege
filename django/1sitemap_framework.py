"""The sitemap framework."""

# initialization after installation
# Urlconf
from django.contrib.sitemaps.views import sitemap

path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

### sitemap for example
from django.contrib.sitemaps
import Sitemap
from blog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date

############# using GenericSitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from blog.models import Entry

info_dict = {
        'queryset': Entry.objects.all(),
        'date_field': 'pub_date',
}

urlpatterns = [
        # some generic view using info_dict
        # ...
        # the sitemap
        path('sitemap.xml', sitemap,
            {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
            name='django.contrib.sitemaps.views.sitemap'),
]

############# sitemap for static views
# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'about', 'license']

    def location(self, item):
        return reverse(item)

# urls.py
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
        'static': StaticViewSitemap,
}

urlpatterns = [
        path('', views.main, name='main'),
        path('about/' views.about, name='about')
        # ...
        path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap')
]

#############
