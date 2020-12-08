""" In views HttpResponse is need. """

from django.http import HttpResponse

def hello_fn(request, name="Word"):
    return HttpResponse("Hello {}!". format(name))

# traditional regular expression syntax for analog 
# In urls.py
    url(r'^hello_fn/(?P<name>\w+)/$', views.hello_fn),
    url(r'^hello-fn/$', views.hello_fn),

# In urls.py for Django 2.0
    path('hello-fn/<str:name>/', views.hello_fn),
    path('hello-fn/', views.hello_fn),

################
from django.views.generic import Views

class HelloView(View):
    def get(self, request, name="World"):
        return HttpResponse("Hello {}!".format(name))

# and urls.py for this
    path('hello-cl/<str:name>/', views.HelloView.as_view()),
    path('hello-cl/', views.HelloView.as_view()),

###############
class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))

class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"

# and urls.py
    path('hello-su/<str:name>/', views.SuperVillainView.as_view()),
    path('hello-su/', views.SuperVillainView.as_view()),


