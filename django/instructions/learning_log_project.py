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

#14 Add URL
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

#20


