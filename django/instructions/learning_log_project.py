"""Retrospective instructions how I work."""

#1 Make a virtual environment

mkdir learning_log
cd learnig_log
pipenv install
pipenv shell  # start a virtual environment

#2 Install Django

pip3 install Django
django-admin.py startproject learning_log .  # dot is important
ls learning_log/  # check how many files in dir

#3 Make a db

python manage.py migrate  # make db.sqlite3

#4 Check how it works
python manage.py runserver  # for http://localhost:8000/
or
python manage.py runserver 8001(etc)  # for another port if 8000 is used

#5 Startapp
into learning_log/
python manage.py startapp learning_logs  # make dir with 'bells and whistles'

#??? Whait, gitignore man!

#6 Gitignore

in place where manage.py:
    touch .gitignore
into the .gitignore:
    settings.py

and remove file from list to commit if you add it yet
    git rm --cached settings.py
    git commit ...

#7 Add class Topic(models.Model) to models.py

#8 Activate model
Add 'learning_logs' to INSTALLED_APPS, before default django apps into settings.py

#9 Change db for Topic(models.Model)
on the place where is file manage.py(base):
    python manage.py makemigrations learning_logs
and we get a migration file 0001_initial.py how make a table on the db

#10 Apply changed data into db
From the base:
    python manage.py migrate

1. Change models.py
2. makemigrations for learning_logs
3. migrate
4. register a model on the admin site, i.e admin.py

#11 Create superuser
From the base:
    python manage.py createsuperuser
    Username:
    Email address:
    Password:
    Password again:

#12 Registered your models on admin.py
from .models import Topic

admin.site.register(Topic)

#13 Check admin site
From base:
    python manage.py runserver

#14 Add an URL
on the file urls.py how is default in the larning_log/

from django.url import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('learning_logs.urls')),
]

# then make second urls.py file into the learnig_logS
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
]

#15 Write view on th views.py

from django.shortcuts import render

def index(request):
    """Home page of app Learning Log"""
    return render(request, 'learning_logs/index.html')

#16 Make templates
on the learning_logs/:
    mkdir templates/learning_logs/index.html

<p>Learning Log</p>
<p>Learning Log help you keep track of your learning, for any topic you`re learning about.</p>

# Restart server

#17 Make a parrent pattern base.html for inheritance
In the same place where is index.html make base.html,
then rewrite index.html for inherit from base.html

#18 Maka a page with list of themes:
First make an URL http://localhost:8000/topics/
Add note to the file learning_logs/urls.py:
    path('topics/', views.topics, name='topics')

then add inherit to the views.py:
    from .models import Topic
    and write:
    def  topic(request)

#18 Maka a template for topics

in the same place where index.html, make topics.html,
then add note to the base.html:
    <a href="{% url 'learning_logs:topics' %}">Topics</a>

Check result in a browser.

#19 Make a pages for are difference themes

First make an URL into learning_logs/usls.py:
    path('topics/<int:topic_id>/', views.topic, name='topic')
then add inherit to the views.py:
    def topic(request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)

# Make template a difference theme
make topic.html

# Add links
into topics.html:
    <li>
      <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}>/a>
    </li>

Voila!

#20 How to add new topic? Make it.

make a forms.py in the same place where models.py

# Make an URL for new topic
learning_logs/urls.py:
    path('new_topic/', views.new_topic, name='new_topic'),

# Make a view for new topic
views.py

# Make a template 
new_topic.html

# Make a link at the topics
topics.html:
    <a href="{%url 'learning_logs:new_topic' %}">Add a new topic:</a>

#21 How to add new note? Make it.

add to forms.py:
    import Entry

    class EntryForm(rorms.ModelForm):
        class Meta:
            model = Entry
            fields = ['text']
            labels = {'text': 'Entry:'}
            widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# Add an URL for new note
urls.py:
    path('new_entry/<int: topic_id>/', views.new_entry, name='new_entry'),

# Add a view for new note
views.py:
    from .forms import EntryForm

    def new_entry(request, topic_id):
        """Add new note to the theme."""
        topic = Topic.objects.get(id=topic_id)
        if request.method != 'POST':
            form = EntryForm()
        else:
            form = EntryForm(data=request.POST)
            if form.is_valid():
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return redirect('learning_logs:topic', topic_id=topic_id)
        context = {'topic': topic, 'form': form}
        return render(request, 'learning_logs/new_entry.html', context)

# Add template
new_entry.py

# Make a link for the new_entry
topic.html:
    <p>
      <a href="{% url 'learning_logs:new_entry' topic.id %}">add new entry</a>
    </p>

#22 Add edit notes posibility.

# Add an URL for edit_entry
learning_logs/urls.py

# Make edit_entry() function
views.py:
    from .models import Entry

    def edit_entry(request, entry_id):
        """Edit existed note."""
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic

        if request.method != 'POST':
            # First query; form is get data from currently note.
            form = EntryForm(instance=entry)
        else:
            # Send data of POST; handle data.
            form = EntryForm(instance=entry, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('learnig_logs:topic', topic_id=topic.id)
        context = {'entry': entry, 'topic': topic, 'form': form}
        return render(request, 'learning_logs/edit_entry.html', context)

# Make a template
edit_entry.html

# Add URL for edit_entry
topic.html

#23 Make a new app - users. http://localhost:8000/users/login/
python manage.py startapp users
ls users

# Add app 'users' to settings.py, for make login/logout page
INSTALLED_APPS:
    'users',

# Add URL 'users' into urls.py
path('', include('learning_logs.usls'))  # before 'learning_logs.urls'

# Make a new file into learning_log/users/
urls.py:
    from django.urls import path, include

    app_name = 'users'
    urlpatterns = [
            path('', include('django.contrib.auth.urls')),
    ]

# Make a template for users
Django by default find template for login/logout in /registrations/
Make it directory, learning_log/users/templates/registration/
And then make login.html

# Make a link to the home page
base.html:
    <a href ="{% url 'learning_logs:topics' %}">Topics</a> -
    {% if user.is_authenticated %}
      >>> Hello, {{ user.username }}.
    {% else %}
      <a href="{% url 'users:login' %}">log in</a>
    {% endif %}

# Go to http://localhost:8000/admin/
log out

# Go to http://localhost:8000/users/login/
log in

#24 After log in make log out page
add to base.html:
    {% if usr.is_authenticated %}
        >>> Hello, {{ user.username }}.
        <a href="{% url 'users:logout' %}">log out</a>
    {% else %}

# Make template for logout in templates/gegistration
logged_out.html

#24 Make an own registration page

# Make URL http://localhost:8000/users/register/
users/urls.py:
    from . import views
    
    path('register/', views.register, name='register'),

# Make a view
/users/views.py:
    def register(request):
        """It's registered new user."""
        if request.method != 'POST':
            # Show empty registration form
            form = UserCreationForm()
        else:
            # Handling data from form
            form = UserCreationForm(data=request.POST)

            if form.is_valid():
                new_user = form.save()
                # Enter and redirect on the home page.
                login(request, new_user)
                return redirect('learning_logs:index')
        # Show empty or not valid form.
        context = {'form': form}
        return render(request, 'users/register.html', context)

# Make a template for register form
/users/templates/register.html

# Make link for registration page
base.html:
    <a href="{% url 'users:register' %}">Register</a> -

#25 Restrict of access

# import Django login_required and decoreate whith it topics()
# It need for login restriction topics from not registered users
learning_logs/views.py

from django.contrib.auth.decorators import login_required

@login_required
def topics(request):
    ...

# change redirect for not registered users
settings.py

LOGIN_URL = '/users/login/'

# And decorate with @login_required all confide pages
views.py

@login_required
def topic(request, topic_id)
...
@login_required
def new_topic(request)
...
@login_required
def new_entry(request, topic_id)
...
@login_required
def edit_entry(request, entry_id)
...

#26 Bind user and his own data
models.py:
    from django.contrib.auth.models import User

    class Topic(models.Model):
        text = model.CharField(max_length=200)
        date_added = models.DateTimeField(auto_now_add=True)
        owner = models.ForeignKey(User, on_delete=models.CASCADE)

# First check how many users is it, and how their id

(env)learning_log$ python manage.py shell

>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ll_admin>, <User: eric>, <User: willie>]>
>>> for user in User.objects.all():
...    print(user.username, user.id)
...
ll_admin 1
eric 2
willie 3
>>>

# Migrate db with id for binding this data with concrete user
python manage.py makemigrations learnig_logs

It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1  # for first variant
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1  # for ll_admin(with id 1)
Migrations for 'learning_logs':
  learning_logs/migrations/0003_topic_owner.py
    - Add field owner to topic

# Make migration
(env)learning_log$ python manage.py migrate

# Check for all ok
python manage.py shell
>>> from learning_logs.models import Topic
>>> for topic in Topic.objects.all():
...    print(topic, topic.owner)

# If you need clear all data in db
python manage.py flush  # and start from zero

#27 How owner may see only his themes?
views.py:  
    # Make restriction views for not owners
    @login_required
    def topics(request):
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')

# Make a checker owner or not sees currently topic
views.py:
    from django.http import Http404

    @login_required
    def topics(request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        if topic.owner != request.user:
            raise Http404

# Safe edit_entry page
views.py:
    @login_required
    def edit_entry(request, entry_id):
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic
        if topic.owner != request.user:
            raise Http404

#28 Add binding new topic with his owner
views.py:
    @login_required
    def new_topic(request):
        if request.method != 'POST':
            form = TopicForm()
        else:
            form = TopicForm(data=request.POST)
            if form.is_valid():
                new_topic = form.save(commit=False)
                new_topic.owner = request.user
                new_topic.save()
                return redirect('learning_logs:topics')

#29 Install django-bootstrap4 for frontend
(env)learning_log$ pip3 install django-bootstrap4

# add bootstrap to settings.py
settings.py:
    INSTALLED_APPS = [
            # My apps
            'learning_logs',
            'users',

            # Another apps
            'bootstrap4',

            # Default django apps
            'django.contrib.admin',
    ]

# Change base.html for bootstrap
base.html:
    {% load bootstrap4 %}
    
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1,
        shrink-to-fit=no">
        <title>Learning Log</title>

        {% bootstrap_css %}
        {% bootstrap_javascript jquery='full' %}
      </head>
      <body>  # make a navigation bar
        <nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">
          <a class="navbar-brand" href="{% url 'learning_logs:index'%}">
          Learning Log</a>
          <button class="navbar=toggler" type="button" data-toggle="collapse"
          data-target="#navbarCollapse" aria-controls="navbarCollapse"
          aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span></button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <a class="nav-link" href="{% url 'learning_logs:topics'%}">
                Topics</a></li>
            </ul>
            <ul class="navbar-nav ml-auto">
              {% if user.is_authenticated %}
                <li class="nav-item">
                  <span class="navbar-text">Hello, {{ user.username }}.</span>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'users:logout' %}">Log out</a
                </li>
              {% else %}
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'users:register' %}">Register</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'users:login' %}">Log in</a></li>
              {% endif %}
            </ul>
          </div>
        </nav>

        <main role="main" class="container">
          <div class="pb-2 mb-2 border-bottom">
            {% block page_header %}{% endblock page_header %}
          </div>
          <div>
            {% block content %}{% endblock content %}
          </div>
        </main>
      </body>
    </html

# Make a 'jumbotron' with buttstrap4
index.html:
    {% extends "learning_logs/base.html" %}

    {% block page_header %}
      <div class='jumbotron'>
        <h1 class="display-3">Track your learning.>/h1>

        <p class="lead">Make your own Learning Log, and keep a list of the
        topics you`re learning about. Whenever you learn something new
        about a topic, make an entry summarizing what you`ve learned.</p>

        <a class="btn btn-lg btn-primary" href="{% url 'users:register' %}"
        role="button">Register &raquo;</a>
      </div>
    {% endblock page_header %}

# Bootstrapped login page
login.html:
    {% load bootstrap4 %}

    {% block page_header %}
      <h2>Log in to your account.</h2>
    {% endblock page_header %}

    {% block content %}
      <form method="post" action="{% url 'users:login' %}" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% buttons %}
          <button name="submit" class="btn btn-primary">Log in </button>
        {% endbuttons %}

        <input type="hidden" name="next"
          value="{% url 'learning_logs:index' %}" />
      </form>
    {% endblock content %}

# amelioration without bootstrapped toppics page
toppics.html:
    {% extends "learning_logs/base.html" %}

    {% block page_header %}
      <h1>Topics</h1>
    {% endblock page_header %}

    {% block content %}
      <ul>
        {% for topic in topics %}
          <li><h3>
            <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
            </h3></li>
        {% empty %}
          <li><h3>No topics have been added yet.</h3></li>
        {% endfor %}
      </ul>
      
      <h3><a href="{% url 'learning_logs:new_topic' %}">Add new topic</h3>
    {% endblock content %}

# Bootstrapped topic.html
topic.html:
    {% extends 'learning_logs/base.html' %}

    {% block page_header %}
      <he>{{ topic }}</h3>
    {% endblock page_header %}

    {% block content %}
      <p>
    <a href = "{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
      </p>

      {% for entry in entries %}
        <div class="card mb-3">
          <h4 class="card-header">
            {{ entry.date_added|date:'M d, Y H:i' }}
            <small><a href="{% url 'learning_logs:edit_entry' entry.id %}">
            edit entry</a></small>
          </h4>
          <div class="card-body">
            {{ entry.text|linebreaks }}
          </div>
        </div>
      {% endfor %}
    {% endblock content %}

#30 Deploy
(env) learning_log$ pip install psycopg2==2.7.*
(env) learning_log$ pip install django_Heroku
(env) learning_log$ pip install gunicorn

(env) learning_log$ pip freeze > requirements.txt  # for Heroku

(env) learning_log$ python --version  # check Python version for requirement.txt

# change settings for Heroku

    # My settings
LOGIN_URL = 'users:login'

    # Settings for Heroku
import django_heroku
django_heroku.settings(locals())

# Make a Procfile where manage.py
Procfile

web: gunicorn leaning_log.wsgi --log-file -

# Go to heroku.com and check your account

# Heroku tell that need Python 3.10 and Postgress locally

# Then install installer for Heroku
$ sudo snap install heroku --classic

pip install psycopg2
pip install gunicorn
pip install django-heroku

# copy examples or file pack from github
$ git clone https://github.com/heroku/python-getting-started.git

# Install Python 3.10
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
(if you need remove then, $ sudo apt autoremove python3.10 --purge)

# Make files when needed
runtime.txt
with note:
python-3.10.4

Procfile
with note:
web: gunicorn gettingstarted.wsgi --log-file -  # for learning_log/wsgi.py

requirements.txt
pip freeze > requirements.txt

# Heroku need PostgreSQl, and I use sqlite in this project. It's fail for deploy? Again.
But I have postrgres
sudo apt-get install postgresql
which psql
$ psql
psql (12.11 (Ubuntu 12.11-0ubuntu0.20.04.1), server 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1))
Type "help" for help.

jack=# \q  # exit

# Ok, change settings for Heroku
settings.py
# My settings
LOGIN_URL = 'users:login'

# Heroku settings
django_heroku.settings(locals())  # it's exactly needed? Read Heroku instructions.
