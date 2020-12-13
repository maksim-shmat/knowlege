""" html for example in Django. """

# base_site.html
Then, edit file and replace {{ site_header|default:_('Django administration') }} with your own site`s name as you see fit. You should end up with a section
of code like:

{% block branding % }
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a>
</h1>
{% endblock %}

###########

