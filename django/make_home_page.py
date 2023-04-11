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
        <li><a href="{% url 'books' %}">All books</a></li>
        <li><a href="{% url 'authors' %}">All authors</a></li>
      </ul>
      {% endblock %}
      </div>
      
      <div class="col-sm-10 ">
      {% block content %}{% endblock %}

      {% block pagination %}
        {% if is_paginated %}
          <div class="pagination">
            <span class="page-links">
              {% if page_obj.has_previous %}
                <a href="{{ request.path }}?page={{
                         page_obj.previous_page_number }}
                         ">Previous</a>
              {% endif %}
              <span class="page-current">
                Page {{ page_obj.number }} from
                     {{ page_obj.paginator.num_pages }}
              </span>
              {% if page_obj.has_next %}
                <a href="{{ request.path }}?page={{
                         page_obj.next_page_number }}
                         ">Next</a>
              {% endif %}
            </span>
          </div>
        {% endif %}
      {% endblock %}

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
        url(r'^book/(?P<pk>/d+)$', views.BookDetailView.as_view(),
                                   name='book-detail'),
        url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
        #   r'book/(?P<stub>[-\w]+)$'  For stubs like /catalog/book/secret_of_power against /catalog/book/33
]

#6 catalog/views.py

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

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

#8 book_detail.html /WebBooks/catalog/templates/catalog/book_detail.html

{% extends "base_generic.html" %}

{% block content %}

  <h1>Name of the book: {{ book.title }}</h1>
  
  <p><strong>Genre:</strong> {{ book.genre }}</p>
  <p><strong>Annotation:</strong> {{book.summary }}</p>
  <p><strong>ISBN:</strong> {{ book.isbn }}</p>
  <p><strong>Language</strong> {{book.language }}</p>
    {% for author in book.author.all %}
      <p><strong>Author:</strong>
        <a href="">{{ author.first_name }}
                   {{ author.last_name }}</a></p>
    {% endfor %}

<div style="margin-left:20px;margin-top:20px">
  <h4>How many exemplars in db</h4>
  {% for copy in book.bookinstance_set.all %}
    <hr><p class="{% if copy.status == 1 %} text-success
                  {% elif copy.status == 2 %} text-danger
                  {% else %} text_warning
                  {% endif %}"> {{ copy.get_status_display }}</p>
    <p><strong>Imprint:</strong> {{copy.imprint}}</p>
    <p class="text-muted"><strong>Number of Invent:</strong> {{copy.id}}</p>
    <p><strong>Status of book exemplar:</strong> {{copy.status}}</p>
  {% endfor %}
</div>
{% endblock %}
<p><strong>Author:</strong> <a href="">{{ author.first_name }}
{{ author.last_name }}</a></p>

#9 autor_list.html /WebBooks/catalog/templates/catalog/autor_list.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>List of authors in db</h1>

  {% if author_list %}
    {% for author in author_list.all %}
    <p>{{ author.first_name }}  {{ author.last_name }},
      <strong>Birth-</strong>{{author.date_of_birth}},
      <strong>Death-</strong>{author.date_of_death}}</p>
    {% endfor %}
  {% else %}
    <p>In db not data author about</p>
  {% endif %}
{% endblock %}
