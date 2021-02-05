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

### creating a sitemap index
from django.contrib.sitemaps import views

urlpatterns = [
        path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
        path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
]

### and more
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page

urlpatterns = [
        path('sitemap.xml',
            cache_page(86400)(sitemaps_views.index),
            {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
        path('sitemap-<section>.xml',
            cache_page(86400)(sitemaps_views.sitemap),
            {'sitemaps': sitemaps}, name='sitemaps'),
]

############ template customization
from django.contrib.sitemaps import views

urlpatterns = [
        path('custom-sitemap.xml', views.index, {
            'sitemaps': sitemaps,
            'template_name': 'custom_sitemap.html'
        }),
        path('custom-sitemap-<section>.xml', views.sitemap, {
            'sitemaps': sitemaps,
            'template_name': 'custom_sitemap.html'
        }, name='django.contrib.sitemaps.views.sitemap'),
]

############ sitemap for example
<?xml version="1.0" encoding="UTF-8"?>
<urlset
    xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
{% spaceless %}
{% for url in urlset %}
    <url>
        <loc>{{ url.location }}</loc>
        {% if url.lastmod %}<lastmod>{{ url.lastmod|dat: "Y-m-d" }}</lastmod>{% endif %}
        {% if url.changefreq %}<changefreq>{{ url.changefreq }}</changefreq>{% endif %}
        {% if url.priority %}<priority>{{ url.priority }}</priority>{% endif %}
        <news:news>
        {% if url.item.publication_date %}<news:publication_date>{{
            url.item.publication_date|date:"Y-m-d" }}</news:publication_date>{% endig %}
        {% if url.item.tags %}<news:keywords>{{ url.item.tags }}</news:keywords>{% endif %}
        </news:news>
    </url>
{% endfor %}
{% endspaceless %}
</urlset>

###############
