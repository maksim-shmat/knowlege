"""Cheat sheet django about."""

#1 pip3

sudo apt install python3-pip

pip3 --version

#2 virtualenv

sudo apt-get install python-virtualenv virtualenv

pip3 install virtualenv

virtualenv -p python3

envgv1

source bin/activate

deactivate

#3 django

git clone git//github.com/django/django django-dev

pip3 install -e django-dev

django-admin --version

django-admin startproject proyect

python manage.py createsuperuser

python manage.py startapp name

python manage.py runserver

pip install -r requirements.txt

python manage.py shell

python manage.py collecstatic

#4 django-database

python manage.py makemigrations

python manage.py migrate

#5 django-leaflet

pip3 install django-leaflet

python manage.py ogrinspect rute.shp --mapping --multi --srid=4326

#6 bower and collecstatic

pip3 install django-bower

rpm install -g bower

python manage.py bower install

pip install django-staticfiles

python manage.py collecstatic

#7 grappelli

pip install django-grappelli

pip instll django-grappelli extras

#8 database django

pip install psycopg2

pip instll psycopg2-binary

#9 git

git init

git clone /path/repository

git clone username@host:/path/repository

git add filename

git add

git commit -m "message"

git push origin master

git remote add origin server

git checkout -b rama (create rama)

git checkout main

git branch -d rama (delete rama)

git push origin rama

git pull

git merge rama

git diff source_rama target_rama

git tag 1.0.0.1b2e1

git log

git checkout --filename

git fetch origin

git reset --hard origin/main

gitk

git config color.ui true

git config format.preety oneline

git add -i
