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

#3 Create base template: index.html in /WebBooks/catalog/templates/index.html


