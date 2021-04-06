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
add to models.py /maksimshmat
def get_absolute_url(self) to class Catetory and class Product

# next
add templates/ structure to /shop
add base.html
add list.html
add detail.html

# next
make static/ in shop/

# next
add no_image.png to static/img/

# next
add to settings.py form maksimshmat/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# next
add a little to urls.py from maksimshmat/
import settings
import static
if settings.DEBUG:

# next

make files structure for magAzine
requirements/_base.txt
requirements/production.txt
requiremente/dev.txt
python3.8 -m pip install -r requirements/dev.txt (download and write big pack)
or python3.8 -m pip freeze > requirements/_base.txt (if you are install all self)

