"""Writing custom API endpoints."""

#1 viws.py
...
from django.shortcuts import render
from ..chapter-3.models import ..., Seller
from rest_framework.permissions import IsAuthenticated
from rest_framework.viws import APIView
...

class GetSellerHTMLView(APIView):
    permission_classes = [IsAuthenticated]
    template_name = 'chapter_8/details/seller.html'

    def get(self, request, format=None, id=0, *args, **kwargs):
        if  request.user.is_authenticated and request.user.has_perm
        ('chapter_3.view_seller'):
            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                seller = None
        else:
            seller = None

        context = {'seller': seller,}

        return render(
                request,
                self.template_name,
                context = context
        )

#2 seller.html
{% load static %}

<h1>Seller Details</h1>

{% if seller %}
  <h2>{{ seller.first_name|safe }} {{
      seller.last_name|safe }}</h3>
  <h3>{{ seller.name|safe }}</h3>

  {% if seller.vehicles %}
    <ul>
      {% for vehicle in seller.vehicles.all %}
        <li>{{ vehicle.fullname }}</li>
      {% endfor %}
    </ul>
  {% endif %}
{% else %}
  <p>
    <b>No Seller to Display</b><br />
    <em>or you <b>DO NOT</b> have permission</em>
  </p>
{% endif %}

#3 site-js.js
function $gotoSPA_Page() {
        ...
        var url = `/chapter-8/seller/${id}/`;

        fetch(url, {
            method: `GET`,
            headers: {
                `Content-Type`: `application/json`,
                }}).then(async(response) => {
                    return await response.text();
                }).then(async(data) => {
                    container.innerHTML = await data;
                });
            }

#4 Mapping the URL pattern
# urls.py
from .views import (
        ...,
        GetSellerView,
        GetSellerHTMLView
)
...
urlpatterns = [
        ...
        path(
            'chapter-8/get-seller/',
            GetSellerView.as_view(),
            name = 'get-seller'
        ),
        path(
            'chapter-8/seller/<int:id>/',
            GetSellerHTMLView.as_view(),
            name = 'seller-detail'
        ),
    ]
