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
########## django.url for home page to template
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', TemplateView.as_view(template_name='homepage.html')),
]

### template homepage.html
<html>
  <body>
    <h4>Home page for Django</h4>
  </body>
</html

############ Permission checks in urls.py for static templates

from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth.models import Group

urlpatterns = [
        url(r'^online/baristas/',
            user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all())
            (TemplateViw.as_view(template_name='online/baristas.html')),name="onlinebaristas"),
        url(r'^online/dashboard/',
            permission_required('stores.add_store')
            (TemplateView.as_view(template_name='online/dashboard.html')),name="onlinedashboard"),
        url(r'^online/',
            login_required(TemplateView.as_view(template_name='online/index.html')),name='online'),
]

###### Permission checks in urls.py for include() definitions

from django.conf.urls import include, url
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern

class DecoratedURLPattern(RegexURLPattern):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedURLPattern, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result


class DecoratedRegexURLResolver(RegexURLResolver):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedRegexURLResolver, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result

def decorated_includes(func, includes, *args, **kwargs):
    urlconf_module, app_name, namespace = includes
    patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
    for item in patterns:
        if isinstance(item, RegexURLPattern):
            item.__class__ = DecoratedURLPattern
            item._decorate_with = func

        elif isinstance(item, RegexURLResolver):
            item.__class__ = DecoratedRegexURLResolver
            item._decorate_with = func

    return urlconf_module, app_name, namespace

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group

from coffeehouse.items.urls import urlpatterns as drinks_url_patterns

urlpatterns = [
        url(r'^items/',
            decoratd_includes(login_required,include(items_url_patterns,namespace="items"))),
        url(r'^stores/',
            decorated_includes(permission_required('stores.add_store'),
            include('coffeehouse.stores.urls',namespace="stores"))),
        url(r'^social/',
            decorated_includes(user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all()),
            include('coffeehouse.social.urls',namespace="social")))<
]

###### Configure urls from django.contrib.auth package

from django.conf.urls import url
from django.contrib.auth import views

# Option 1 to include all urls (See option 2 for included urls)
urlpatterns = [
        url(r'^accounts/', include('django.contrib.auth.urls')),
]

# Option 2) (Explicit urls, all included in django.contrib.auth)
urlpatterns = [
        url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
        url(r'^accounts/logout/$', views.LogoutViews.as_view(), name='logout'),

        url(r'^accounts/password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
        url(r'^accounts/password_change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

        url(r'^accounts/password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
        url(r'^accounts/password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_/-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        url(r'^accounts/reset/done/$', views.PasswordResetCompleteViw.as_view(), name='password_reset_complete'),
]

###### Configure url for user up workflow
# urls.py main

from django.conf.urls import url
from django.contrib.auth import views
from coffeehouse.registration import views as registration_views

urlpatterns = [
        url(r'^accounts/', include('django.contrib.auth.urls')),
        url(r'^accounts/signup/$',registration_views.UserSignUp.as_view(),name="signup"),
]

###### The permalink Decorator example

from django.conf.urls.defaults import *
from django.views.generic.detail import DetailView
from library.import models

class LibraryDetail(DetailView):
    queryset = models.Article.objects.all()

urlpatterns = patterns('django.views.generic',
        url(r'^articles/(?P<object_id>\d+)/$', LibraryDetail.as_view(),
            name='library_article_detail'),
)

# a corresponding model (located in a library application) might look like this:
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField()

    def get_absolute_url(self):
        return ('library_article_detail',
                (), {'object_id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)

###### Positional vs keyword arguments
# for example, in th URL pattern was defined as r'^articles/(d+)/$'

The permalink decorator => return ('library_articles_detail', (self.id,), {})
The url template tag => {% url library_article_detail article.id %}
The reverse() function => reverse('library_article_detail', args=(1,))

###### Use Lots of Arguments
# simple for now

from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Post

def show_post(request, id):
    post = Post.objects.get(id=id)
    context = RequestContext(request, {'post': post})
    return render_to_response('blog/detail.html', context)

# better
from django.shortcuts import render_to_response
from django.template import RequestContext

def show_object(request, id, model, template_name):
    object = model._default_manager.get(pk=id)
    context = RequestContext(request, {'object': object)})
    return render_to_response(teplate_name, context)

### url configuration
from django.conf.urls.defaults import *
from blog.models import Post

urlpatterns = patterns('',
        (r'^post/(?P<id>\d+)/$', 'blog.views.show_object', {
            'model': Post,
            'template_name': 'blog/detail.html',
        }),
)

###### Applying View Decorators

from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from thirdpartyapp.views import special_view

urlpatterns = patterns(''
        (r'^private/special/$', login_required(special_view)),
)

###### Writing a View Decorator

from django.utils.functional import wraps

def set_test_cookie(view):
    """
    Automatically sets the test cookie on all anonymous users, 
    so that they can be logged in more easily, without having
    to hit a separate login page.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous():
            request.session.set_test_cookie()
        return view(request, *args, **kwargs)
    return wraps(view)(wrapper)

### extract code form the beginning or end of a set of views

from django.utils.functional import wraps
from django.shortcuts import get_object_or_404

from news.models import Article

def get_article_from_id(view):
    """
    Retrieves a specific article, passing it to the view directly
    """
    def wrapper(request, id, *args, **kwargs):
        article = get_object_or_404(Article, id=int(id))
        return view(request, article=article, *args, **kwargs)
    return wraps(view)(wrapper)

### 
from django.utils.functional import wraps
from mylogapp.models import Entry

def logged(view):
    """
    Logs any errors that occurred during the view
    in a special model design for app-specific errors
    """
    def wrapper(request, *args, **kwargs):
        try:
            return view(request, *args, **kwargs)
        except Exception as e:
            # Log the entry using the application's Entry model
            Entry.objects.create(path=request.path,
                                 type='View exception',
                                 description=str(e))
            # Re-raise it so standard error handling still applies
            raise
    return wraps(view)(wrapper)

###### Individual View Methods

def view(request, template_name='form.html'):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form here
            return redirect('success')
        else:
            return render(request, template_name, {'form': form})
        else:
            form = ExampleForm() # no data gets passed in 
            return render(request, template_name, {'form': form})

### and class-based view instead
class FormView(View):
    template_name = 'form.html'

    def get(self, request):
        form = ExampleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form here
            return redirect('success')
        else:
            return render(request, self.template_name, {'form': form})

###### url configuration for Contacts

from django.cont.urls.defaults import *
from django.views.generic import ListView, DetailView

from contacts import models, views

urlpatterns = patterns('',
        url(r'^$',
            ListView.as_view(queryset=models.Contact.objects.all(),
                             template_name='contacts/list.html',
                             paginate_by=25),
            name='contact_list'),
        url(r'^add/$', views.EditContact.as_view(
            template_name='contacts/editor_form.html',
            ), name='contact_add_form'),
        url(r'^(?P<slug>[\w-]+)/$',
            DetailView.as_view(queryset=models.Contact.objects.all(),
                               slug_field='user__username',
                               template_name='contacts/list.html'),
            name='contact_detail'),
        url(r'^(?P<username>[\w-]+)/edit/$', views.EditContact.as_view(
            template_name='contacts/editor_form.html',
            ), name='contact_edit_form'),
)

######
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from properties import models

urlpatterns = patterns('',
        url(r'^$',
            ListView.as_view(queryset=models.Property.objects.listed(),
                             template_name='properties/list.html',
                             paginate_by=25),
            name='property_list'),
)

###
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from properties import models

urlpatterns = patterns('',
        url(r'^$',
            ListView.as_view(queryset=models.Property.objects.listed(),
                             template_name='properties/list.html',
                             paginate_by=25),
            name='property_list'),
        url(r'^(?P<slug>\d+-[\w-]+-\d+)/$',
            DeatailView.as_view(queryset=models.Property.objects.listed(),
                                slug_field='slug',
                                template_name='properties/detail.html'),
            name='property_detail'),
)

#1 urls dinamic vs hardcode

<a href="(% url 'index' %}">Home</a>  # better than hardcode

< href="/catalog/">Home</a>  # Hard Code

#2
