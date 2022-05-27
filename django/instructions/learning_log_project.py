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

#
