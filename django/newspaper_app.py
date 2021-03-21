""" Continue after auth.py etc."""

$ python manage.py startapp articles

### newspaper_project/settings.py
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'djanog.contrib.messages',
        'django.conttib.staticfiles',

        # 3rd Party
        'crispy_forms',

        # Local
        'users.apps.UsersConfig',
        'pages.apps.PagesConfig',
        'articles.apps.AritclesConfig', # new
]

TIME_ZONE = 'America/New_Yourk' # new

### articles/models.py

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

### make a new migration
$ python manage.py makemigrations articles
$ python manage.py migrate

### articles/admin.py
from django.contrib import admin
from .models import Article  # or from . import models

admin.site.register(Article)
# or # admin.site.register(models.Article)

###
$ python manage.py runserver

### newspaper_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('users/', include('django.contrib.auth.urls')),
        path('articles/', include('articles.urls')), # new
        path('', include('pages.urls')),
]

### $ touch articles/urls.py
from django.urls import path

from .views import ArticleListView  # or from . import views

urlpatterns = [
        path('', AricleListView.as_view(), name='aritcle_list'),
]

### articles/views.py
from django.views.generic import ListView
from .models import Article  # or from . import models

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

### $ touch templates/article_list.html
{% extends 'base.html' %}

{% block title %}Articles{% endblock title %}

{% block content %}
  {% for article in object_list %}
    <div class="card">
      <div class="card-header">
        <span class="font-weight-bold">{{ article.title }}</span> &middot;
        <span class="text-muted">by {{ article.author }} |
        {{ article.date }}</span>
      </div>
      <div class="card-body">
        {{ article.body }}
      </div>
      <div class="card-footer text-center text-muted">
        <a href="#">Edit</a> | <a href="#">Delete</a>
      </div>
    </div>
    <br />
  {% endfor %}
{% endblock content %}

### Edit/Delete
# articles/urls.py
from django.urls import path
from .views import (   # or from . import views
        ArticleListView,
        ArticleUpdateView,
        ArticleDetailView,
        ArticleDeleteView, # new
)

urlpatterns = [
        path('<int:pk>/edit/',
            ArticleUpdateView.as_view(), name='article_edit'), # new
        path('<int:pk>/'
            ArticleDetailView.as_view(), name='article_detail'), # new
        path('<int:pk>/delete/',
            ArticleDeleteView.as_view(), name='article_delete'), # new
        path('', ArticleListView.as_view(), name='article_list'),
]

### articles/views.py
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView # new
from django.urls import reverse_lazy # new

from .models import Article  # or from . import models

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeteteView(DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

### add new templates
$ touch templates/article_detail.html
$ touch templates/article_edit.html
$ touch templates/article_delete.html

### template/article_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="article-entry">
    <h2>{{ object.author }} | {{ object.date }}</p>
      <p>by {{ object.author }} | {{ object.date }}</p>
      <p>{{ object.body }}</p>
  </div>

  <p><a href="{% url 'article_edit' article.pk %}">Edit</a> |
    <a href="{% url 'article_delete' article.pk %}">Delete</a></p>
  <p>Back to <a href="{% url 'article_list' %}">All Articles</a>.</p>
{% endblock content %}

### templates/article_edit.html
{% extends 'base.html' %}

{% block content %}
  <h1>Edit</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
  <button class="btn btn-info ml-2" type="submit">Update</button>
  </form>
{% endblock content %}

### templates/article_detete.html
{% extends 'base.html' %}

{% block content %}
  <h1>Delete</h1>
  <form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ article.title }}"?</p>
    <button class="btn btn-danger ml-2" type="submit">Confirm</button>
  </form>
{% endblock %}

### templates/article_list.html
...
<div class="card-footer text-center text-muted">
  <a href="{% url 'article_edit' article.pk %}">Edit</a> |
  <a href="{% url 'article_delete' article.pk %}">Delete</a>
</div>
...

### Create page
# articles/views.py
...
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
...
class ArticleCreateView(CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)

### articles/ursl.py
from django.urls import path

from .views import (
        ArticleListView,
        ArticleUpdateView,
        ArticleDetailView,
        ArticleDeleteView,
        ArticleCreateView, # new
)

urlpatterns = [
        path('<int:pk>/edit/',
            ArticleUpdateView.as_view(), name='article_edit'),
        path('<int:pk>/',
            ArticleDetailView.as_view(), name='article_detail'),
        path('<int:pk>/delete/',
            ArticleDeleteView.as_view(), name='article_delete'),
        path('new/', ArticleCreateView.as_view(), name='article_new'), #new
        path('', ArticleListView.as_view(), name='article_list'),
]

### $ touch templates/article_new.html

{% extends 'base.html' %}

{% block content %}
  <h1>New article</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <button class="btn btn-success ml-2" type="submit">Save</button>
  </form>
{% endblock content %}

### templates/base.html
...
<body>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
    <a class="navbar-brand" href="{% url 'home' %}">Newspaper</a>
    {% if user.is_authenticated %}
    <ul class="navbar-nav mr-auto">
      <li class="nav-item"><a href="{% url 'article_new' %}">+ New</a></li>
    </ul>
    {% endif %}
    <button class="navbar-toggler" type="button" data-toggle="collapse" date-tar\
            get="#navbarCollapse" aria_controls="navbarCollapse" aria-expanded="false" aria-\
            label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            ...

# templates/home.html
{% extends 'base.html' %}

{% block title %}Home{% endblock title %}

{% block content %}
<div class="jumbotro">
  <h1 class="display-4">Newspaper app</h1>
  <p class="lead">A Newspaper website built with Django.</p>
  <p class="lead">
    <a class="btn btn-primary btn-lg" href="{% url 'aritcle_list' %}"
    role="button">View All Articles</a>
  </p>
</div>
{% endblock content %}

###
