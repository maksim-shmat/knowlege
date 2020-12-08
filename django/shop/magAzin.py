""" magAzin.py """

mkdir django2
python3.8 -m venv virt1
source virt1/bin/activate
mkdir django_cms
cd django_cms
python3.8 -m pip install --upgrade pip

python3.8 -m pip install django
>>> import django
>>> print(django.get_version())
python3.8 -m pip install django-cms
python3.8 -m pip install djangocms-admin-style


django-admin.py startproject myproject
settings.py
add 'sekizai' and more, gide: http://docs.django-cms.org/en/latest/how_to/install.html
urls.py

pip install psycopg2 # for Postgre(later)
python manage.py migrate # make db(SQLite3)
python manage.py createsuperuser

python manage.py cms check
settings.py


make files structure for magAzine
requirements/_base.txt
requirements/production.txt
requiremente/dev.txt
python3.8 -m pip install -r requirements/dev.txt (download and write big pack)
or python3.8 -m pip freeze > requirements/_base.txt (if you are install all self)

