"""Regular expression for django url patterns."""

url(r'^$',...)  Empty string(Home page)  Matches: http://127.0.0.1/


url(r'^stores/',...)  Any trailing characters  Matches: http://127.0.0.1/stores/  http://127.0.0.1/stores/long+string+anything+12345


url(r'^about/contact/$',...)  Exact, no trailing characters  Matches: http://127.0.0.1/about/contact  Doesn`t match: http://127.0.0.1/about


url(r'^stores/\d+/'...)  Numbers  Matches: http://127.0.0.1/stores/2/  http://127.0.0.1/stores/34/  Doesn`t match: http://127.0.0.1/drinks/324/


url(r'^drinks/\D+/',...) Non-digits  Matches: http://127.0.0.1/drinks/mocha/  Doesn`t match: http://127.0.0.1/drinks/324/


url(r'^drinks/mocha|espresso/',...)  Word options, any trailing characters  Matches: http://127.0.0.1/drinks/mocha/  http://127.0.0.1/drinks/mochaccino/  http://127.0.0.1/drinks/espresso/  Doesn`t match: http://127.0.0.1/drinks/soda/


url(r'^drinks/mosha$|espresso/$',...)  Word options exact, no trailing characters  Matches: http://127.0.0.1/drinks/mocha/  Doesn`t match: http://127.0.0.1/drinks/mochaccino/  Matches: http://127.0.0.1/drinks/espresso/  Doesn`t match: http://127.0.0.1/drinks/espressomacchiato/


url(r'^stores/\w+/',...)  Word characters (Any letter lower or uppercase,
number, or underscore)  Matches: http://127.0.0.1/stores/sandiego/  http://127.0.0.1/stores/LA/  http://127.0.0.1/stores/1/  Doesn`t match: http://127.0.0.1/san-diego/


url(r'^stores/[\w]+/',...)  Word characters or dash  Matches: http://127.0.0.1/san-diego/


url(r'^state/[A-Z]{2}/',...)  Two uppercase letters  Matches: http://127.0.0.1/CA/  Doesn`t match: http://127.0.0.1/Ca/

### django url parameter definition for access in templates
urlpatterns = [
        url(r'^drinks/(?P<drink_name>/D+)/', TemplateView.as_view(template_name='drinks/index.
        html')),
]

####### add extra options in the url
url(r'^drinks/(?P<drink_name>/D+)', TemplateView.as_view(template_name='drinks/index.html'), {'onsale': True}),

####### django url parameter definition for access in view methods in
# main urls.py file
# project main urls.py
from coffeehouse.stores import views as stores_views

urlpatterns = patterns[
        url(r'^stores/(?P<store_id>\d+)/',stores_views.detail),
]

###### django view method in views.py to access url parameter
from django.shortcuts import render

def detail(request,store_id):
    # Access store_id with 'store_id' variable
    return render(request, 'stores/detail.html')

###### django url with optional parameters leveraging the same view method
from coffeehouse.stores import views as stores_views

urlpatterns = patterns[
        url(r'^stores/',stores_views.detail),
        url(r'^stores/(?P<store_id>\d+)/',stores_views.detail),
]

####### django view method in views.py with default value
from django.shortcuts import render

def detail(request,store_id='1'):
    # Access store_id with 'store_id' variable
    return render(request,'stores/detail.html')

# extra options from url definition
def detail(request,store_id='1',location=None):
###
url(r'^stores/',stores_view.detail,{'location': 'headquarters'})

###### django.view method extracting url parameters with request.GET
from django.shortcuts import render

def detail(request,store_id='1',location=None):
    # Access store_id param with 'store_id' variable and location param
    # with 'location' variable
    # Extract 'hours' or 'map' value appended to url as
    # ?hours=sunday&map=flash
    hours = request.GET.get('hours', '')
    map = request.GET.get('map', '')
    # 'hours' has value 'sunday' or '' if hours not in url
    # 'map' has value 'flash' or '' if map not in url
    return render(request, 'stores/detail.html')

####### django urls.py with no url consolidation
from django.conf.urls import url
from django.views.generic import TemplateView
from coffeehouse.about import views as about_views
from coffeehouse.stores import views as stores_views

urlpatterns = [
        url(r'^$',TemplateView.as_view(template_name='homepage.html')),
        url(r'^about/',about_views.index),
        url(r'^about/contact/',about_views.contact),
        url(r'^stores/',stores_views.index),
        url(r'^stores/(?P<store_id>\d+)/',stores_views.detail,{'location':'headquarters'}),
]

### django urls.py with include to consolidate urls
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$',TemplateView.as_view(template_name='homepage.html')),
        url(r'^about/',include('coffeehouse.about.urls')),
        url(r'^stores/',include('coffeehouse.stores.urls'),{'location':'headquarters'}),
]

####### django /coffeehouse/about/urls.py loaded via include
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index),
        url(r'^contact/$',views.contact),
]

### django urls.py with inline include statements
from django.conf.urls import include, url
from django.views.generic import TemplateView

from coffeehouse.about import views as about_views
from coffeehouse.stores import views as stores_views

store_patterns = [
        url(r'^$',stores_views.index),
        url(r'^(?P<store_id>\d+)/$',stores_views.detail),
]

about_patterns = [
        url(r'^$',about_views.index),
        url(r'^contact/$',about_views.contact),
]

urlpatterns = [
        url(r'^$',TemplateView.as_view(template_name='homepage.html')),
        url(r'^about/',include(about_patterns)),
        url(r'^stores/',include(store_patterns),{'location':'headquarters'}),
]

###### django url using name
# definition in urls.py
url(r'^$', TemplateView.as_view(template_name='homepage.html'),name="homepage")

# definition in view method
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

def method(request):
    ...
    return HttpResponsePermanentRedirect(reverse('homepage'))

# definition in template
<a href="{% url 'homepage' %}">Back to home page</a>

### django url with arguments using name
# definition in urls.py
url(r'^drinks/(?P<drink_name>\D+)/',TemplateView.as_view(template_name='drinks/index.html'),name="drink"),

# definition in view method
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

def method(request):
    ...
    return HttpResponsePermanentRedirect(reverse('drink', args=(drink.name,)))

# definition in template
<a href="{% url 'drink' drink.name %}">Drink in sale</a>

<a href="{% url 'drink' 'latte' %}">Drink on sale</a>

###### django urls.py with namespace attribute
# Main urls.py
from django.conf.urls import include, url

urlpatterns = [
        url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
        url(r'^about/',include('coffeehouse.about.urls',namespace="about")),
        url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
]

# About urls.py
from . import views

urlpatterns = [
        url(r'^$',views.index,name="index"),
        url(r'^contact/$',views.contact,name="contact"),
]

# Stores urls.py
from . import views

urlpatterns = [
        url(r'^$',views.index,name="index"),
        url(r'^(?P<store_id>\d+)/$',views.detail,name="detail"),
)

# definition in view method
from django.http import HttpResponsePernamnentRedirect
from django.core.urlresolvers import reverse

def method(request):
    ...
    return HttpResponsePermanentRedirect(reverse('about:index'))

# definition in template
<a href="{% url 'stores:index' %}">Back to stores index</a>

###### django urls.py with nested namespace attribute
# Main urls.py
from django.conf.urls import include, url
from django.views.generic import  TemplateView

urlpatterns = [
        url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
        url(r'^(?P<store_id>\d+)/$', views.detail,name="detail"),
        url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="about")),
]
# About urls.py
from . import views

urlpatterns = [
        url(r'^$',views.index,name="index"),
        url(r'^contact/$',views.contact,name="contact"),
]

# definition in view method
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

def method(request):
    ...
    return HttpResponsePermanentRedirect(reverse('stores:about:index', args=(store.id,)))

# definition in template
<a href="{% url 'stores:about:index' store.id %}">See about for {{store.name}}</a>

#########
