"""Start Django project about."""

#1 Linux and python3.x

check

#2 Postgresql

sudo apt-get install postgresql-11
mkdir freelance_python
cd freelance_python/

#3 venv

sudo apt-get install python3-venv
python3.8 -m venv myvenv
source myvenv/bin/activate

#4 use cookiecutter without standard django-admin startproject

pip install cookiecutter
cokiecutter https://github.com/pydanny/cookiecutter-django

### Ansver questions

project_name [My Awesome Project]: Python Freelance Project Scanner
project_slug [python_freelance_projects_scanner]: freelance_python
description [Behold My Awesome Project!]: Python freelance projects scanner
author_name [Daniel Roy Governer]: Pussan Chook
domain_name [example.com]: furfur.com
email [zorro@puss.com] you@puppy.com
version [0.1.0]:
Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 3
timezone [UTC]: UTC+7
window [n]:
use_pycharm [n]: y
use_docker [n]:
Select postgresql_version:
    1 - 11.3
    2 - 10.8
    3 - 9.6
    4 - 9.5
    5 - 9.4
Chose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 1
Select js_task_runner:
    1 - None
    2 - Gulp
Choose from 1, 2 (1, 2) [1]:
Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
Choose from 1, 2, 3 (1, 2, 3) [1]: 3
custom_bootstrap_compilation [n]:
use_compressor [n]:
use_celery [n]:
use_mainhog [n]:
use_sentry [n]:
use_whitenoise [n] y
use_heroku [n]
use_travisci [n] y
keep_local_envs_in_vcs [y]  n
debug [n]:
    [WARNING]: You chose not to use a cloud provider, media files won`t be served in production.
    [SUCCESS]: Project initialized, keep up the good work!

#5 Use VCS(Version Control System) git

git init
git config --global user.email "me@chunka.com"
git config --global user.name "Zork Awsm"
git remote add origin https://github.com/zork-awsm/pstroun.git  # make it repohandle on github
git add.
git commit -m 'Intitial commit'
git push -u origin master

#6 Install requirements

pip install -r requirements/local.txt

#7 Make Postgre db

sudo -u postgres psql

CREATE USER myprojectuser WITH PASSWORD '1234very|strong';
CREATE DATEBASE myproject OWNER myprojectuser;
\q

#8 Make migrations

export DATABASE_URL="postgres://myprojectuser:difficultpassword@localhost/myproject"
./manage.py migrate

#9 start server

./manage.py runserver


