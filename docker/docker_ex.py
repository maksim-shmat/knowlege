"""Examples Dockerfile and docker-compose.yml."""

###### Docerfile 1
FROM ubuntu:16.04

# bring system up-to-date
RUN apt-get update -qq&&\
        apt-get upgrade -qqy

# install a particular version of Python and other stuff
RUN apt-get install -qqy\
        python-virtualenv\
        libpq-dev\
        python3=3.5.*\
        python3-dev=3.5.*

# copy scripts into the container for convenience(you could mount a folder as well)
RUN mkdir -p/srv
ADD start.sh/srv/start.sh
RUN chmod +x/srv/start.sh
ADD maintenance.sh/srv/maintenance.sh
RUN chmod +x/srv/maintenance.sh

# tell the container to execute the start script
ENTRYPOINT["/bin/bash", "/srv/start.sh"]

###### docker-compose.yml
version:'2'

volumes:
  postgres_data:{}
  env:{}

services:
  app:
    build:./compose/app_dev
    volumes:
      - ./baa:/srv/app
      - env:/srv/env
    working_dir:/srv/app
    env_file
      - env_dev
      - env_dev_secret
    ports:
      - "127.0.0.1:5000:5000"
      depends_on:
        - db
        - redis
      # uncommennt for debugging the service-container does not try to start dev server
      # entrypoint:["sh","-c","sleep infinity"]
    db:
      # https://hub.docker.com/_/postgres/
      image:postgres:9.6.3
      volumes:
        - postgres_data:/var/lib/postgresql/data
      environment:
        POSTGRES_USER:postgres
        POSTGRES_PASSWORD:dbpw
      ports:#make db accessible locally
        - "127.0.0.1:5432:5432"
      redis:
          # https://hub.docker.com/_/redis/
          image:redis:3.2.9
          ports:#make redis accessible locally
            - "127.0.0.1:6379:6379"

###### NOT USE ROOT use USER
FROM ubuntu:18.04
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

###### Run PostgreSQL in side a docker-compose.yaml
version: "3"
services:
  db:
    image: "postgres:11"    # POSTGRES
    container_name: "postgres"
    ports:
      - "5432:5432"    # from local port to the container port
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  dbdata:

# and $ docker-compose up -d db # for run db
docker-compose logs db # inspect
docker ps # see postgres container
docker volume ls | grep dbdata # run docker volume
docker-compose exec db psql -U postgres # connect to the PostgreSQL
# postgres=#

###
postgres=# create database wordcount;
CREATE DATABASE

postgres=# \l

### create a role in db
docker-compose exec db psql -U postgres wordcount
wordcount=# CREATE ROLE wordcount_dbadmin;
CREATE ROLE
wordcount=# ALTER ROLE wordcount_dbadmin LOGIN;
ALTER ROLE
wordcount=# ALTER USER wordcount_dbadmin PASSWORD 'MYPASS';
ALTER ROLE
postgres=# \q

### change requirements.txt
for your Postgres:
    change psycopg2 version
    change redis version for Python version support
    change rq pagage for Python version support

### Dockerfile for this
# cat Dockerfile
FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgesql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

COPY . .

ENTRYPOINT [ "python" ]
CMD ["app.py"]

###### Example migrate for flask
# cat docker-compose.yaml
version: "3"
services:
  migrations:
    image: "flask-by-example:v1"
    command: "manage.py db upgrade"
  environment:
    APP_SETTINGS: config.ProductionConfig
    DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
  depends_on:
    - db
db:
  image: "postgres:11"
  container_name: "postgres"
  ports:
    - "5432:5432"
  volumes:
    - dbdata:/var/lib/postgresql/data
volumes:
  dbdata:

###### Ports fo Django 8000, and 5000 flask
# django ex
version: '3.7'
services:
  veb:
    build: app
    ports:
      - '8000:8000'
######
#how add redis in docker-compose.yaml
redis:
  image: "redis:alpine"
  ports:
    - "6379:6379"

###
docker-compose up -d redis

######
create a service called worker for the Python RQ

worker:
  image: "flask-by-example:v1"
  command: "worker.py"
  environment:
    APP_SETTINGS: config.ProductionConfig
    DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    REDISTOGO_URL: redis://redis:6379
  depends_on:
    - db
    - redis

###
docker-compose up -d worker

######
create a new service called "app" in docker-compose.yaml

app:
  image: "flsk-by-example:v1"
  command: "manage.py runserver --host=0.0.0.0"
  ports:
    - "5000:5000"
  environment:
    APP_SETTINGS: config.ProductionConfig
    DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    REDISTOGO_URL: redis:6379
  depends_on:
    - db
    - redis

######
# final version docker-compose.yaml
version: "3"
services:
  app:
    image: "griggheo/flask-by-example:v1"
    command: "manage.py runserver --host=0.0.0.0"
    ports:
      - "5000:5000"
    environment:
      APP_SETTINGS: config.ProductionConfig
      DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
      REDISTOGO_URL: redis://redis:6379
    depends_on:
      - db
      - redis
  worker:
    image: "griggheo/flask-by-example:v1"
    command: "worker.py"
    environment:
      APP_SETTINGS: config.ProductionConfig
      DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
      REDISTOGO_URL: redis://redis:6379
    depends_on:
      - db
      - redis
  migration:
    image: "griggheo/flask-by-example:v1"
    command: "manage.py db upgrade"
    environment:
      APP_SETTINGS: config.ProductionConfig
      DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    depends_on:
      - db
  db:
    image: "postgres:11"
    container_name: "postgres"
    ports:
      - "5432:5432"
    volumes:
      -dbdata:/var/lib/postgresql/data
  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
volumes:
  dbdata:

######
