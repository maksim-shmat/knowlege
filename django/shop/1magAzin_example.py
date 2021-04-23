""" magAzin.py """

mkdir django
python3.8 -m venv virt3    # make a virtual environment
source virt3/bin/activate

mkdir maksim.shmat
python3.8 -m pip install --upgrade pip

python3.8 -m pip install django
>>> import django
>>> print(django.get_version())
"""
python3.8 -m pip install django-cms
python3.8 -m pip install djangocms-admin-style
У них свой магаз приложений и по ходу свой хостинг, так что задеплоить на heroku наверное будет trubles. Мб потом. 
"""
# next
django-admin.py startproject maksimshmat
cd maksimshmat
django-admin startapp shop
settings.py
INSTALLED_APPS =[
        ...
        'shop.apps.ShopConfig',

# next
add class Category and class Product in models.py

# next
python3.8 -m pip install Pillow

# next
python manage.py makemigrations
python manage.py migrate

# next
add @admin.register(Category) and (Product) into admin.py

# next
python manage.py createsuperuser
username (leave blank to use 'jack')
Email address: m.sh@
Password:
Password(again)

# next
add to views.py
def product_list()
def product_detail()

# next
add paths to urls.py by /shop

# next
add templates/shop/base.html
add templates/shop/product/detail.html list.html

# next
make static/ in shop/

# next
add no_image.png to static/img/

# next
add to settings.py form maksimshmat/
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR, 'media/'

# next
add a little to urls.py from maksimshmat/
import settings
import static
if settings.DEBUG:

# next
That`s it simple site now.

# next
make files structure for magAzine where there README.md
requirements/base.txt
requirements/production.txt
requiremente/dev.txt
python3.8 -m pip install -r requirements/dev.txt (download and write big pack)
or python3.8 -m pip freeze > requirements/_base.txt (if you are install all self)
-it is for download all pip programms for project

# next 
add --- local.env --- with Django project configuration
Debug=True
# syntax: DATABASE_URL=psql://username:password@127.0.0.1:8458/database
DATABASE_URL=sqlite:///db.sqlite3
SECRET_KEY="*************"

# next
make file --- requirements.txt --- for memory?
Django>=1.7
django-environ>=0.3.0
django-braces>=1.4.0
django-crispy-forms>=1.4.0
django-admin-bootstrapped>=1.6.9
django-debug-toolbar>=1.2.1

# next
make file --- dev-requirements.txt
-r requirements.txt
# Extra stuff required for local dev
pudb==2014.1

# next
in settings.py write:
    SECRET_KEY = env('SECRET_KEY')

# next
add base.css to static/css  # it is fone
