""" This model online courses may be knowledge db for my org. """

python manage.py dumpdata courses --indent=2
mkdir courses/fixtures
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
python manage.py loaddata subjects.json

( {% load staticfiles %} and {% load admin_static %}) #is old school and not
# support Django 3.0. Change it {% load static %}
Or add this to settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

pylint
pynsource model.py
pyreverse -p png shop


python3.8 -m pip install django-braces

You are trying to add a non-nullable field 'file' to image without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 0
Please select a valid option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1
Migrations for 'courses':
  courses/migrations/0004_auto_20201116_1228.py
    - Remove field url from image
    - Add field students to course
    - Add field file to image
    - Create model Video
'

python3.8 -m pip install django-embed-video

sudo apt install memecached
python3.8 -m pip install python-memcached
python3.8 -m pip install django-memcache-status

python3.8 -m pip install djangorestframework

sudo apt install nginx
The end.
