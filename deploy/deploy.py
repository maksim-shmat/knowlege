"""Deploy Django about."""

# first make settings.py two variables for DEBUG True/False
if DEBUG is True:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
            Path(BASE_DIR, "/static/")
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/var/www/static/'
    STATICFILES_DIRS = [
            Path(BASE_DIR, '/var/www/static/')
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, '/var/www/ /media/')

###### work with git
pip freeze > requirements.txt
make .gitignore

git init
git add .gitignore
git commit -m "gitignore"
git add *
git commit -m "initial commit"
git remote add origin your_remote_repo_url
git remote -v
git push origin master

###### work on server
go to Digital Ocean
ssh root@your_IP_address

sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install apache2
sudo apt install python-pip3 pyenv #?
sudo apt install python-setuptools python-dev build-essential
sudo apt install libapache-mod-wsgi-py3
sudo apt build-dep python-imaging
sudo apt install python3-pip3 apache2 libapache2-mod-wsgi-py3

cd /var/www
mkdir venv && cd venv #?
virtualenv -p python3 .
source bin/activate
python - -version

### update settings.py for static and media paths
if DEBUG is True:
    STATIC_URL = '/static/'
    STATIC_ROOT = '/static/'
    STATICFILES_DIRS = [Path(BASE_DIR, "static")]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, 'media')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = '/var/www/venv/BookProject/pizzaproject/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = Path(BASE_DIR, '/var/www/venv/BookProject/pizzaproject/media/')

######
git commit -m "updates to settings.py"
git push origin master
git clone you_remote_git_repo

######
cd pizzaproject
python manage.py migrate
python manage.py createsuperuser

###### For change project to deploy instruction
1. git add files-you-want-to-add(in your local git repository on your machine)

2. git commit -m "message"

3. git push origin master

4. Log in to the server with ssh root@your-ip

5. cd /var/www/venv (get into the venv directory and activate the virtual environment)

6. git pull origin master (to fetch updates from a remote repo, run this command in your project directory on a server)

7. python manage.py collectstatic (if you need to update static files on a server, make sure you run this command from your Django project on a server)

8. service apache2 restart

######
replace default configurations with our settings for apache

sudo nano /etc/pache2/sites-available/000-default.conf

###### 755 for everyone hacker read and write on your site, CHANGE IT!
sudo adduser $USER www-data
sudo chown www-data:www-data /var/www/venv/BookProject/pizzaproject
sudo chown www-data:www-data /var/www/venv/BookProject/pizzaproject/db.sqlite3
sudo chmod -R 775 /var/www/venv/BookProject/pizzaproject

### work with media
cd media
mkdir pizzeriaImages
sudo chmod 777 /var/www/venv/BookProject/pizzaproject/media/pizzeriaImages
python manage.py collectstatic
service apache2 restart

######
