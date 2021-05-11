"""Drop secret key, and begin from zero."""

make git repo

######
mkdir code && cd code
mkdir hello && cd hello

pipenv install django

pipenv shell

django-admin.py startproject hello_project

python manage.py runserver # check

######
django-admin startapp pages
settings.py 
INSTALLED_APPS =[
        ...
        'pages.apps.PagesConfig',
        ]
######
hello_project/urls.py
from django.urls import path, insclude # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
    ]
######
pages/urls.py
from django.urls import path
from .views import home_page_view

urlpatterns = [
        path('', home_page_view, name='home')
]

######
pages/views.py
from django.http import HttpResponse

def home_page_views(request):
    return HttpResponse('Hello, World!')

#####################
touch Dockerfile
---------------
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

CODE Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY . /code/

###
docker build .

###
touch docker-compose.yml
------------------------
# version is now using "compose spec"
# v2 and v3 are now combined!
# docker-compose v1.27+ required

services:
  web:
    build: .
    command: python /code/manage.py runserver 127.0.0.1:8000
    volumes:
      - .:/code
    ports:
      - 8000:8000

###
docker-compose up
docker-compose down

####################

(hello) $ python manage.py migrate

docker-compose up -d

docker-compose exec web python manage.py createsuperuser

username:
email:
password:

###
docker-compose down

docker-compose.yml
add note about db
-----------------
  env_file:
    - ./.env.dev
  depends_on:
    - db
db:
  image: postgres:13
  volumes:
    - postgres_data:/var/lib/postgresql/data/
  environment:
    - POSTGRES_USER=hello_django
    - POSTGRES_PASSWORD=hello_django
    - POSTGRES_DB=hello_django_dev
volumes:
  postgres_data:

###
docker-compose up -d

settings.py
------------
DATABASES = {
        'default': {
            'ENGINE': env("SQL_ENGINE"),
            'NAME': env("SQL_DATABASE"),
            'USER': env("SQL_USER"),
            'PASSWORD': env("SQL_PASSWORD"),
            'HOST': env("SQL_HOST"),
            'PORT': env.int("SQL_PORT")
    }
}

###
docker-compose up -d --build

docker-compose exec web pipenv install psycopg2-binary
docker-compose down
docker-compose up -d --build
незавёлся постгрес этот чорт не указал реквизиты
#################
settings.py for .env.dev
-----------------------------
from environs import Env # new

env = Env() # new
env.read_env(env_file=root_path(".env.dev")) # new

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])['.herokuapp.com', 'localhost', '127.0.0.1']

DJANGO_DATABASE_URL = env.db("DATABASE_URL")
DATABASES = {
        "default": env.dj_db_url("DATABASE_URL")}
TIME_ZONE = env.str("TIME_ZONE", default="America/Chicago")

### 
make .env.dev file
------------------
DEBUG=1
SECRET_KEY="****"
ALLOWED_HOSTS='.herokuapp.com', 'localhost', '127.0.0.1'
DJANGO_USERNAME='jack'
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER='postgres'
SQL_PASSWORD='postgres'
SQL_HOST='db'
SQL_PORT=5432
DATABASE_URL=psql://postgres:postgres@127.0.0.1:8000/database
#DATABASE_URL=psql://username:password@127.0.0.1:8000/database
TIME_ZONE="America/Chicago"
