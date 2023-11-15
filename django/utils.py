"""File for Django, app realize ratings."""

#1 bookr/reviews/utils.py

def average_rating(rating_list):
    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list))

#2 views.py

from django.shortcuts import render, get_object_or_404

from .models import Book
from .utils import average_rating


def index(request):
    return render(request, "base.html")

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request,
            "reviews/search-results.html",
            {"search_text": search_text})

#3 books_list.html

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Bookr</title>
</head>
  <body>
    <h1>Book Reviw application</h1>
    <hr>
...

#4 urls.py

from django.urls import path
from . import views


urlpatterns = [
        path('books/', views.book_list,
            name='book_list'),
]


