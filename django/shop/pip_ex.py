"""Pip about."""

pip freeze>requirements.txt  # write all dependecies in file

pip + venv = Pipenv

requirements.txt = Pipfile and Pipfile.lock

pipenv -h  # help

1. pip install pipenv
2. pipenv shell
3. exit

# next
I think install all programs handle from venv3, but it be with open versions,
not fixed. Memento!

# next 
and requirements.txt need it? Not need man.
there are pipenv install -r requirements.txt yeah?

# next
Download from github example (requests lib)
$ pipenv install -e git+https://github.com/requests/requests.git#egg=requests

# next
install in setarate pack --dev, not into the dev pack programs
$ pipenv install pytest --dev 

# next
pipenv lock ???

# next
pipenv graph
pipenv praph --reverse # all dependancies

# next
pipenv open psycopg2 (for example, open programm into editor)
pipenv run <insert command here> ( for example python manage.py runserver)

# next
check version of programm
pipenv check

# next
pipenv uninstall --all
pipenv uninstall --all-dev

# next
generate requirements.txt from Pipenv
pipenv lock -r > requirements.txt
pipenv lock -r -d > dev-requirements.txt
