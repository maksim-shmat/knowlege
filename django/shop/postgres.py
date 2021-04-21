"""About db."""

sudo apt-get install postgresql postgresql-contrib
# but should install in venv or docker?

# next 2
python3.8 -m pip install psycopg2-binary

settings.py
import psycopg2

DATABASE_URL = ?os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

python3.8 -m pip install dj-database-url

add to --- requirements.txt --- 
psycopg2-binary
dj-database-url

# next 3
su postgres
createuser -dP blog

createdb -E utf8 -U blog blog

# next 4
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blog',
            'USER': 'blog',
            'PASSWORD': '****',
        }
}

# next 5
python manage.py migrate
python manage.py createsuperuser

#
