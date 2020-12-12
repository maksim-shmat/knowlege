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

