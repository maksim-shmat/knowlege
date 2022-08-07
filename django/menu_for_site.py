"""Create django site menu."""

#1
# /pages/views.py
#...
context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg_update_date,
        'page_list': Page.objects.all(),
}
#...

#2 Template
# mfdw_site/templates/base.html
#...
<nav id="nav">
  <ul>
    {% block sidenav %}
    <li>Menu 1</li><li>Menu 2</li><li>Menu 3</li>
    {% endblock sidenav %}
  </ul>
</nav>
# ...

#3 Template
# /pages/templates/pages/page.html

# ... {% endblock title %}

    {% block sidenav %}
      {% for page in page_list %}
      <li>
        <a href="{{ page.permalink }}">{{ page.title }}</a>
      </li>
      {% endfor %}
    {% endblock sidenav %}

  {% block content %}
# ...

#4
