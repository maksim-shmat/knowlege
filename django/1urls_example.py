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

