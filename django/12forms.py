"""Second file about forms."""

###### Now forms step by step

### templates/base.html
{% load staticfiles %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400"
    rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class='nav-right'>
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>

### Alternative sintax base.html
{% load staticfiles %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" rel/="stylesheet">
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
  </head>
  <body>
    <div class="container">
      <header>
        <div class="nav-left">
          <h1><a href="/">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>

### Create view
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
#   fields = '__all__'   # alternative

### further $ touch templates/post_new.html
{% extends 'base.html' %}

{% block content %}
  <h1>New post</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
  </form>
{% endblock content %}

### add an import on the second line for reverse get_absolute_url() and __str__()
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

### $ touch templates/post_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="post-entry">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
  </div>

  <a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a>
{% endblock content %}

### Alternative
{% extends 'base.html' %}

{% block content %}
  <h1>Edit post</h1>
  <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
  <input type="submit" value="Update" />
</form>
{% endblock %}

### blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']  # or '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

### blog/urls.py
from django.urls import path
from .views import(    # or from . import views
        BlogListView,
        BlogDetailView,
        BlogCreateView,
        BlogUpdateView,
)

urlpatterns = [
        path('post/<int:pk>/edit/',
            BlogUpdateView.as_view(), name='post_edit'),
        path('post/new/', BlogCreateView.as_view(), name='post_now'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('', BlogListView.as_view(), name='home'),
]

### templates/post_detail.html
{% extends 'base.html' %}

{% block content %}

    <div class="post-entry">
      <h2>{{ post.title }}</h2>  # or object.title
      <p>{{ post.body }}</p>     # or object.body
    </div>

    <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
    <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
{% endblock content %}

### $ touch templates/post_delete.html
# templates/post_delete.html
{% extends 'base.html' %}

{% block content %}
  <h1>Delete post</h1>
  <form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <input type="submit" value="Confirm" />
  </form>
{% endblock %}

###### blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy

from .models import  Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']   # or '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

### blog/urls.py
from django.urls import path

from .views import (    # or from . import views
        BlogListView,
        BlogUpdateView,
        BlogDeleteView,
        BlogCreateView,
        BlogDeleteView, # new
)

urlpatterns = [
        path('post/<int:pk>/delete/', # new
            BlogDeleteView.as_view(), name='post_new'),
        path('post/new/', BlogCreateView.as_view(), name='post_new'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('post/<int:pk>/edit/',
            BlogUpdateView.as_view(), name='post_edit'),
        path('', BlogListView.as_view(), name='home'),
]

###### Declaring and Identifying Fields

from django import forms

class ContactForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if not user.is_authenticated():
            # Add a name field since the user doesn't have a name
            self.fields['name'] = forms.CharField(label='Full name')

###### Binding to User Input

from my_app.forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
    else:
        form = MyForm()
    ...

### for FILES
from my_app.forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
    else:
        form = MyForm()
    ...

######
