"""Work with Django, make home page."""

#1 urls.py

from django.urls import path
from .import views

urlpatterns = [
        path('', views.index, name='index'),
]

# it for that
# <href="{% url 'index' %}">Home</a>  # better than hard code

# hard code not good
#<href="/catalog/">Home</a>

#2 catalog/views.py

from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Author, BookInstance, Genre


def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()

    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           'num_visits': num_visits},
                  )

#3 Create base template: base_generic.html in /WebBooks/catalog/templates/base_generic.html

<!DOCTYPE html>
<html lang="en">
<head>
  {% block title %}<title>Shmat Store</title>{% endblock %}
  <meta charset="utr-8">
  <meta name="viewport" content="width=device-width,
                        initial-scale=1">
  <link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/
    bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/
              jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/
              js/bootstrap.min.js"></script>

  <!-- Add static CSS-file -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
  {% block head %}
    <img src="{% static 'images/logotip.jpg' %}"
    style="width:100px; height:100px;" align="absmiddle">
    <font size=7, color="blue">Site "Shmat Store"</font>
  {% endblock %}
</head>

<body>
  <div class="container-fluid">

    <div class="row">
      <div class="col-sm-2">
      {% block sidebar %}
      <ul class="sidebar-nav">
        <li><a href="{% url 'index' %}">Head page</a></li>
        <li><a href="">All books</a></li>
        <li><a href="">All authors</a></li>
      </ul>
      {% endblock %}
      </div>
      
      <div class="col-sm-10 ">
      {% block content %}{% endblock %}
      {% block footer %}
        {% block copyright %}
      <p>Copyright OOO "Mans and books", 2023. All rights reserved</p>
        {% endblock %}
      {% endblock %}
      </div>
    </div>
  </div>
</body>
</html>

#4 create index.html in /WebBooks/catalog/templates/index.html
# names in templates the same names from view, content(dict)
# content={'num_books': num_books,
          #'num_instances': num_instances,
          #'num_insatances_available': num_instances_available,
          #'num_authors': num_authors}

{% extends "base_generic.html" %}

{% block content %}
<h1>Head page</h1>

  <p>Welcome to <em>Shmat Store</em>, It is simple web-site, readed on Django,
     it is project for fun.</p>
  
  <h2>Dinamical content</h2>

    <p>Data base of site Shmat Store contain next strings:</p>
    <ul>
      <li><strong>How many books:</strong> {{ num_books }}</li>
      <li><strong>How many exemplars of books:
          </strong> {{ num_instances }}</li>
      <li><strong>How many exemplars in cart:
          </strong> {{ num_instances_available }}</li>
      <li><strong>How many authors of books:
          </strong> {{ num_authors }}</li>
    </ul>
{% endblock %}

#5 /WebBooks/urls.py

from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf.urls import url


urlpatterns = [
        path('', views.index, name='index'),
        path('admin/', admin.site.urls),
        url(r'^books/$', views.BookListView.as_view(), name='books'),
]

#6 catalog/views.py

from django.views import generic

class BookListView(generic.ListView):
    model = Book

#7 /WebBooks/catalog/templates/catalog/book_list.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>List of books from db</h1>
  {% if book_list %}
  <ul>
    {% for book in book_list %}
    <li>
      <a href="{{ book.get_absolute_url }}">
               {{ book.title }}</a>
               ({{book.genre}})
    </li>
    {% endfor %}
  </ul>
  {% else %}
    <p>Not books in db</p>
  {% endif %}
{% endblock %}

#8 
