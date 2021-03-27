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

###### Validating Input

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Do mare work here, since the data is known to be good
        else:
            form = MyForm()
        ...

###### Using Class-Based Views

from django.shortcuts import render, redirect

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request, 'form.html', {'form': form})

### better
from django.shortcuts import render, redirect
from django.views.generic.base import View

class MyView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request, 'form.html', {'form': form})

### better more
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

class MyView(FormView):
    form_class = MyForm
    template_name = 'form.html'
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super(MyView, self).form_valid(form)

### 
from django.views.generic import edit
from my_app.models import MyModel

class CreateObject(edit.CreateView):
    model = MyModel

    class EditObject(edit.UpdateView):
        model = MyModel

    class DeleteObject(edit.DeleteView):
        model = MyModel
        success_url = '/'

###### forms validation

from django.forms import fields, uril

class LatitudeField(fields.DecimalField):
    default_error_messages = {
            'out_of_range': u'Value must be within -90 and 90.',
    }

    def clean(self, value):
        value = super(LatitudeField, self).clean(value)
        if not -90 <= value <= 90:
            raise util.ValidationError(self.error_messages['out_of_range'])
        return value


class LongitudeField(fields.DecimalField):
    default_error_messages = {
            'out_of_range': u'Value must be within -180 and 180.',
    }

    def clean(self, value):
        value = super(LatitudeField, self).clean(value)
        if not -180 <= value <= 180:
            raise util.ValidationError(self.error_messages['out_of_range'])
        return value

###### Rendering HTML

from django import forms

class PriceInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        return '$ %s' % super(PriceInput, self).render(name, value, attrs)

class PercentInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        return '%s %%' % super(PercentInput, self).render(name, value, attrs)

class ProductEntry(forms.Form):
    sku = forms.IntegerField(label='SKU')
    description = forms.CharField(widget=forms.Textarea())
    price = form.DecimalField(decimal_places=2, widget=PriceInput())
    tax = forms.IntegerField(widget=PercentInput())

print ProductEntry()

"""
<tr><th><label for="id sku">SKU:</label></th><td<>input type="text" name="sku" id="id_sku" /></td></tr>
<tr><th><label for="id_description">Description:</label></th><td><textarea id="id_description" rows="10" cols="40" name="description"></textarea></td></tr>
<tr><th><label for="id_price">Price:</label></th><td>$ <input type="text" name="price" id="id_price" /></td></tr>
<tr><th><label for="id_tax">Tax:</label></th><td><input type="text" name="tax" id="id_tax" /> %</td></tr>
"""
######
