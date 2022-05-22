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

in place where manage.py
touch .gitignore
into the .gitignore:
    ~/django2/knowlege/django/learning_log/learning_log/settings.py
    or
    django/learning_log/learning_log/settings.py

and remove file from list to commit if you add it yet
git rm --cached settings.py
git commit ...

#
