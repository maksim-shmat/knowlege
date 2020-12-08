$ git clone https://github.com/DjangoPatternsBook/superbook2.git

pip install -U pip
pip install pipenv

cd superbook2
pipenv install --dev  # broken Dec 1 check later
pipenv shell

cd src
python manage.py migrate
python manage.py createsuperuser
jack
shm@
huesoska
python manage.py runserver


