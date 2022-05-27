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
        # Page for add new topic
        path('new_topic/', views.new_topic, name='new_topic'),
        # Page for add new note
        path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
        # Page for edit note
        path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
