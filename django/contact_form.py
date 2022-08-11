"""Add 'Contact us' form on the site."""

#1 Template
# pages/templates/pages/contact.html

{% extends "pages/page.html" %}

{% block title %}Contact Us{% endblock title %}

{% block content %}
<h1>Contact us</h1>

{% if submitted %}
  <p class="success">
    Your message was submitted successfully. Thank you.
  </p>

{% else %}
  <form action="" method="post" novalidate>
  <table>
    {{ form.as_table }}
    <tr>
      <td>&nbsp;</td>
      <td><input type="submit" value="Submit"></td>
    </tr>
  </table>
  {% csrf_token %}
  </form>
{% endif %}
{% endblock content %}

#2 Create the Contact form view
# pages/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Page
from .forms import ContactForm

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
        else:
            form = ContactForm()
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'pages/contact.html',
                {'form': form, 'page_list': Page.objects.all(),
                    'submitted': submitted})

#3 Make the form prettier with some CSS
# main.css
# ...
ul.errorlist {
        margin: 0;
        padding: 0;
}
.errorlist li {
        border: 1px solid red;
        color: red;
        background: rgba(255, 0, 0, 0.15);
        list-style-position: inside;
        display: block;
        font-size: 1.2em;
        margin: 0 0 3px;
        padding: 4px 5px;
        text-align: center;
        border-radius: 3px;
}

input, textarea {
        width: 100%;
        padding: 5px!important;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        border-radius: 3px;
        border_style: solid;
        border_width: 1px;
        border-color: rgb(169,169,169)
}

input {
        height: 30px;
}
.success {
        background-color: rgba(0, 128, 0, 0.15);
        padding: 10px;
        text-align: center;
        color: green;
        border: 1px solid green;
        border-radius: 3px;
}
