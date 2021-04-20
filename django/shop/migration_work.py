"""About migration."""

# next Try clean migrations
python manage.py migrate <app_name> zero
python manage.py makemigrations <app_name>
python manage.py migrate <app_name>


