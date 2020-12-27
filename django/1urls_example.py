""" Urls call path(). """

# for polls/urls.py for example from Django docs
from django.urls import path
from . import views

app_name = 'polls'  # add app to namespaces your URLconf
urlpatterns = [
        path ('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
]

##############
# Here's a sample URLconf:
from django.urls import path
from . import views

urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        path('articles/<int:year>/', views.year_archive),
        path('articles/<int:year>/<int:month>/', views.month_archive),
        path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]

###############
#Registering custom path converters.

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
# Register custom converter classes in your URLconf using register_converter()

from django.urls import path, register_converter
from . import converters, views

register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        path('articles/<yyyy:year>/', views.year_archive),
        ...
]
###############
# Using regular expressions
from django.urls import path, re_path
from . import views

urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
        re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.month_archive),
        re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/{?P<slug>
        [/w-]+)/$', views.article_detail),
]
###############
# Man regurlar exspresion is ugly, serious man.
from django.urls import re_path

urlpatterns = [
        re_path(r'^blog/(page-(\d+)/)?$', blog_articles),  # bad
        re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),#good
]
############
# Including other URLconfs
from django.urls import include, path

urlpatterns = [
        # ... snip ...
        path('community/', include('aggregator.urls')),
        path('contact/', include('contact.urls')),
        # ... snip ...
]

###
# Another possibility is to include additional URL patterns by using a list
# of path() instances.
from django.urls import include, path
from apps.main imort views as main_views
from credit import views as credit_views

extra_patterns = [
        path('reports/', credit_views.report),
        path('reports/<int:id>/', credit_views.report),
        path('charge/', credit_views.charge),
]

urlpatterns = [
        path('', main_views.homepage),
        path('help/', include('apps.help.urls')),
        path('credit/', include(extra_patterns)),
]
###
from django.urls import path
from . import views

urlpatterns = [
        path('<page_slug>-<page_id>/history/', views.history),
        path('<page_slug>-<page_id>/edit/', views.edit),
        path('<page_slug>-<page_id>/discuss/', views.discuss),
        path('<page_slug>-<page_id>/permissions/', views.permissions),
]
###
from django.urls import include, path
from . import views

urlpatterns = [
        path('<page_slug>-<page_id>/', include([
            path('history/', views.history),
            path('edit/', views.edit),
            path('discuss/', views.discuss),
            path('permissions/', views.permissions),
        ])),
]
########
# In settings/urls/main.py
from django.urls import include, path

urlpatterns = [
        path('<username>/blog/', include('foo.urls.blog')),
]

# In foo/urls/blog.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.blog.index),
        path('archive/', views.blog.archive),
]

#########
# The path() function can take an optional third argument which should be a
# dictionary of extra keyword arguments to pass to the view function.

from django.urls import path
from . import views

urlpatterns = [
        path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]

#########
# Passing extra options to include()
# set one:
# main.py
urlpatterns = [
        path('blog/', include('inner'), {'blog_id': 3}),
]
# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
        path('archive/', views.archive),
        path('about/', views.about),
]

# set two:
# main.py
from django.urls import include, path
from mysite import views

urlpatterns = [
        path('blog/', include('inner')),
]
# inner.py
from django.urls import path

urlpatterns = [
        path('archive/', views.archive, {'blog_id': 3}),
        path('about/', views.about, {'blog_id': 3}),
]
##########
# Reverse resolution of URLs

from django.urls import path
from . import views

urlpatterns = [
        # ...
        path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
        # ...
]

###
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
# Or with the year in a template context variable: 
<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a>
</li>
{% endfor %}
</ul>

###
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

###########
# URL namespaces and included URL confs
# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<ink:pk>/', views.DetailView.as_view(), name='detail'),
]
###
# urls.py
from django.urls import include, path

urlpatterns = [
        path('polls/', include('polls.urls')),
]
###########
# add include() path
from django.urls import include, path
from . insert views

polls_patterns = ([
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
], 'polls')

urlpatterns = [
        path('polls/', include(polls_patterns)),
]
##########

