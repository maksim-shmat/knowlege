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
      -./baa:/srv/app
      -env:/srv/env
    working_dir:/srv/app
    env_file
      -env_dev
      -env_dev_secret
    ports:
      -"127.0.0.1:5000:5000"
      depends_on:
        -db
        -redis
      # uncommennt for debugging the service-container does not try to start dev server
      # entrypoint:["sh","-c","sleep infinity"]
    db:
      # https://hub.docker.com/_/postgres/
      image:postgres:9.6.3
      volumes:
        -postgres_data:/var/lib/postgresql/data
      environment:
        POSTGRES_USER:postgres
        POSTGRES_PASSWORD:dbpw
      ports:#make db accessible locally
        -"127.0.0.1:5432:5432"
      redis:
          # https://hub.docker.com/_/redis/
          image:redis:3.2.9
          ports:#make redis accessible locally
            -"127.0.0.1:6379:6379"

######
