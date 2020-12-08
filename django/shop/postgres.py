mkdir django-postgres
cd django-postgres

python -m venv env
env/scripts/activate   # win?

pip install django
pip freeze
env/scripts/activate

django-admin startproject postgresTest
cd postgresTest
python manage.py startapp testdb

python manage.py runserver
open pgAdmin4 in filemanager and make db

Go to settings.py
INSTALLE_APPS  <add 'testdb',>

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dbtest',
            'USER': 'postgres',
            'PASSWORD': '1234',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
}

test/db/models.py

from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

pip install psycopg2

manage your db with pgAdmin
