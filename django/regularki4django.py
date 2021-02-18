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

#######
