"""Docker and Django, postgres, gunicorn."""

#1 Make dir of project

mkdir django-docker-joker && cd django-docker-joker

mkdir app && cd app

python3.9 -m venv venv  # or pipenv

source venv/bin/activate

#2 Install Django

(venv) pip install django==3.2.3
django-admin.py startproject config .
python manage.py migrate

#3 Start

python manage.py runserver
go to http://localhost:8000/

#4 rm venv...  what?

#5 make a file requirements.txt into /app/
## add django==3.2.3

#6 rm db.sqlite3 from /app/

#7 look at dir:

app > config>__init__.py, asgi.py, settings.py, urls.py, wsgi.p
    > manage.py
    > requirements.txt

#8 Install Docker and add Dockerfile into /app/

-----------docker file
# app/Dockerfile
# pull the official docker image
FROM python:3.9.5-slim

# set work directory
WORKDIR/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

----------------

#9 Add docker-compose.yml  into /

-----------docker-compose.yml
# docker-compose.yml
version:'3.8'
services:
    web:
        build: ./app
        command: python manage.py runserver 0.0.0.0:8000
        volume:
            - ./app:/app
        ports:
            - 8008:8000
        environment:
            - DEBUG=1

#10 make an image

docker-compose build

#11 run container

docker-compose up -d
# and go to http://localhost:8008
# check errors into docker-compose logs -f

#12 add new strings into docker-compose docker about

-------------docker-compose.yml
# docker-compose.yml
version: '3.8'
services:
    web:
        build: ./app
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py runserver 0.0.0.0:8000'
        volumes:
            - ./app:/app
        ports:
            - 8008:8000
        environment:
            - DEBUG=1
            - DATABASE_URL=postgresql://django_traefik:django_traefik@db:5432/django_traefik
        depends_on:
            - db
        db:
            image: postgres:13-alpine
            volumes:
                - postgres_data:/var/lib/postgresql/data/
            expose:
                - 5432
            evironment:
                - POSTGRES_USER=django_traefik
                - POSTGRES_PASSWORD=django_traefik
                - POSTGRES_DB=django_traefik

volumes:
    postgres_data:

#13 Add new strings to requirements.txt

---------------requirements.txt
Django==3.2.3
django-environ==0.4.5
psycopg2-binary==2.8.6
---------------

#14 initialization config/settings.py

---------
# config/settings.py
import environ
env = environ.Env()
---------

#15 Add dict DATABASES

--------
# config/settings.py

DATABASES = {'default': env.db(),}
--------

#16 Rewrite variable DEBUG

--------
# config/settings.py

DEBUG = env('DEBUG')
--------

#17 Make new image and run both containers

docker-compose up -d --build

#18 Run first migration

docker-compose exec web python manage.py migrate --noinput

#19 Check that default db is it.

docker-compose exec db psql --username=django_traefik --dbname=django_traefik
psql (13.2)
Type "help" for help.
django_traefik=# \1

List of databases
Name  |  Owner  | Encoding  |  Collata  | Ctype  |  Access privileges

django_traefik  | django_traefik  | UTF8  |  en_US.utf8  |  en_US.utf8  
postgres  |  django_traefik  |  UTF8  |  en_US.utf8  |  en_US.utf8  |
...

#20 Check that volume is it

$ docker volume inspect django-docker-traefik_postgres_data

#21 Add Gunicorn into requirements.txt

---------
Django==3.2.3
django-environ==0.4.5
gunicorn==20.1.0
psycopg2-binary==2.8.6
---------

#22 Make prodaction docker-compose file

---------
# docker-compose.prod.yml

version: '3.8'
services:
    web:
        build: ./app
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; gunicorn --bind 0.0.0.0:8000 config.wsgi'
        ports:
            - 8008:8000
        environment:
            - DEBUG=0
            - DATABASE_URL=postgresql://django_traefik:django_traefik:5432/django_traefic
        depends_on:
            - db
    db:
        image: postgres:13-alpine
        volumes:
            - postgres_data_prod:/var/lib/postgresql/data/
        expose:
            - 5432
        environment:
            - POSTGRES_USER=django_traefik
            - POSTGRES_PASSWORD=django_traefik
            - POSTGRES_DB=django_traefik

volumes:
    postgres_data_prod:
---------

#23 rm containers from dev and volumes with -v, what?

docker-compose down -v

#24 Make work images and run containers

$ docker-compose -f docker-compose.prod.yml up -d --build

#25 Run migrations

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

#26 Check errors

docker-compose -f docker-compose.prod.yml logs -f

#27 Make a new Dockerfile.prod

-------------
# app/Dockerfile.prod

###########
# BUILDER #
###########

# pull official base image

FROM python:3.9.5-slim as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies

RUN apt-get update && apt-get install -y --no-install-recommends gcc

# lint

RUN pip install --upgrade pip
RUN pip install flake8==3.9.1
COPY . .
RUN flake8 --ignore=E501,F401 .

# install python dependencies

COPY requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

########
# FINAL#
########

# pull official base image

FROM python:3.9.5-slim

# create directory for the app user

RUN mkdir -p /home/app

# create the app user

RUN addgroup --system app && adduser --system --group app

# create the appropriate directories

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project

COPY . $APP_HOME

# chown all the files to the app user

RUN chown -R app:app $APP_HOME

# change to the app user

USER app
------------

#28 Renew web into docker-compose.prod.yml for Docker.prod

------------
web:
    build:
        context: ./app
        dockerfile: Dockerfile.prod
    command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; gunicorn --bind 0.0.0.0:8000 config.wsgi'
    ports:
        - 8008:8000
    environment:
        - DEBUG=0
        - DATABASE_URL=postgresql://django_traefik:django_traefik@5432/django_traefik
    depends_on:
        - db
------------

# 29 try next commands

$ docker-compose -f docker-compose.prod.yml down -v

docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noimput

#30 Traefik it is a HTTP-proxy and balancer (Traefik vs Nginx)
# add file traefik.dev.toml

-------------
# traefik.dev.toml

# listen on port 80
[entryPoints]
  [entryPoints.web]
  address = ":80"

# Traefik dashboard over http
[api]
insecure = true

[log]
level = "DEBUG"

[accessLog]

# containers are not discovered automatically
[providers]
  [providers.docker]
    exposedByDefault = false
-------------

#31 Renew docker-compose.yml and add traefik:

-------------
# docker-compose.yml
version: '3.8'

services:
    web:
        build: ./app
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py runserver 0.0.0.0:8000'
        volumes:
            - ./app:/app
        expose: # new
            - 8000
        environment:
            - DEBUG=1
            - DATABASE_URL=postgresql://django_traefik:django_traefik@db:5432/django_traefik
        depends_on:
            - db
        labels: # new
            - "traefik.enable=true"
            - "traefik.http.routers.django.rule=Host(`django.localhost`)"
        db:
            image: postgres:13-alpine
            volumes:
                - postgres_data:/var/lib/postgresql/data/
            expose:
                - 5432
            environment:
                - POSTGRES_USER=django_traefik
                - POSTGRES_PASSWORD=django_traefik
                - POSTGRES_DB=django_traefik
        traefik: # new
            image: traefik:v2.2
            ports:
                - 8008:80
                - 8081:8080
            volumes:
                - "$PWD/traefik.dev.toml:/etc/traefik/traefik.toml"
                - "/var/run/docker.sock:/var/run/docker.sock:ro"
volumes:
    postgres_data:
---------------

#32 for check 
# first down all containers

$ docker_compose down -v
$ docker_commpose -f docker-compose.prod.yml down -v

#33 Make a new images

$ docker-compose up -d --build

go to hppp://django.localhost:8008/
and check django.localhost:8081  # for traefik

# stop it
$ docker-compose down -v


