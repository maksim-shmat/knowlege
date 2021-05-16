"""find is environ module."""

Just one second:
    pipenv install django-environ... and... ModuleNotFoundError: No module named 'environ'

    What? Ok.

python3
>>> help('modules')
        django - check
        docker - check
        pathlib - check
        hello_project - check
        django-environ - no
        environ - no
        environs - NO
        wtf?
###
pipenv shell
python3
>>> help('modules')
        environ - check

>>> help('environ')

DJANGO_POSTGRES = 'django.db.backends.postgresql'
REDIS_DRIVER = 'django_redis.cache.RedisCache'
VERSION = '0.4.5'
logger = <Logger environ.environ (WARNING)>

FILE
    /home/jack/.local/share/virtualenvs/hello_project-Xcq3Hbk_/lib/python3.8/site-packages/environ/__init__.py

###
pipenv run pip freeze
django-environ==0.4.5
