"""urls.py for learning_logS/."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        # Page with list of all themes
        path('topics/', views.topics, name='topics'),
        # Page with info about different theme
        path('topics/<int:topic_id>/', views.topic, name='topic'),
]
