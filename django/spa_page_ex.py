"""Building Single Page Aplication(SPA) like page, with Django REST."""

#1 create view
...
from django.template.response import TemplateResponse
from django.views.generic import View
...

class GetSellerView(View):
    template_name = 'chapter_8/spa_pages/get_seller.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return TemplateResponse(
                request,
                self.template_name,
                context
        )

#2 Building the template

# /becoming_a_django_entdev/chapter_8/templates/chapter_
#8/spa_pages/get_seller.html
{% extends 'chapter_8/base/base_template_1.html' %}
{% load static %}
...
{% block body_content %}
  <form>
    <div class="field-box input-box">
      <label for="seller-id">Seller ID:</label>
      <div class="form-group">
        <input id="seller-id" type="text" />
        <span class="help-text">Please enter 
        the ID of the seller you want to lookup</span>
      </div>
    </div>
    <button type="button" id="get-sellers" onclick ="$gotoSPA_Page()">
    Get Seller Details</button>
  </form>

  <div id="details">
    <p>!!! No Details to Display !!!</p>
  </div>
{% endblock %}

#3 Writing with JavaScript

# /becoming_a_django_entdev/chapter_8/static/chapter_8/js/site-js.js
function $gotoSPA_Page() {
        const input = document.getElementById(
            'seller-id'
        );
        const container = document.getElementById(
            'details'
        );
        const id = input.value;
        var url = `/chapter-8/seller/${id}/`;
        fetch(url, {
            method; 'GET',
            headers: {
                'Content-Type': 'application/json',
        }}).then(response => {
            return response.json();
        }).then(data => {
            container.innerHTML = JSON.stringify(data);
        });
}

#3.1 async JavaScript
# site-js.js
function $gotSPA_Page() {
        ...
        fetch(url, {
            method: `GET`,
            headers: {
                `Content-Type`: `application/json`,
            }
        }).then(async(response) => {
            return await response.json();
        }).then(async(data) => {
            const thisData = await data;
            container.innerHTML = JSON.stringify(
                thisData
            );
        });
}

#4 urls.py
from .views import ..., GetSellerView
...
urlpatterns = [
        ...
        path(
            'chapter-8/get-seller/',
            GetSellerView.as_view(),
            name = 'get-seller'
        ),
]
