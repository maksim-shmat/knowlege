"""App orders shop about."""

python manage.py startapp orders

INSTALLED_APPS = [
        ...
        'orders.apps.OrdersConfig',
]

# next
make models.py

# next
python manage.py makemigrations
python manage.py migrate

# next
