"""Template styling with Bootstrap.

https://getbootstrap.com/docs/4.4/getting-started/introduction/.
"""


#1
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,
    initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href=
    "https://stackpath.bootstrapcdn,com/bootstrap/4.4.1/
    css/bootstrap.min.css" integrity="sha384-
    Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNVygBiFeWPGFN9M
    uhOf23Q9Ifjh" crossorigin="anonymous">
  </head>
    <body>
      <h1>Welcome to my Site</h1>
      <button type="button" class="btn btn-primary">
      Checkout my Blog!</button>
    </body>
</html>

#2 adding template inheritance and a Bootstrap navigation bar

# base.html
<!doctype html>
{% load static %}
<html lang="en">
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,
  initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
...
# book_list.html
{% extends 'base.html' %}

{% block content %}
<ul class="list-group">
  {% for item in book_list %}
  <li class="list-group-item">
    <span class="text-info">Title: </span> <span>{{
        item.book.title }}</span>
    <br>
    <span class="text-info">Publisher:
        </span><span>{{
            ierm.book.publisher }}</span>
...
#
