"""Create Django user from shell."""

$ python manage.py shell

from django.contrib.auth.models import User


user = User.objects.create_user('user01', 'user01@example.com',
        'user01password')
user.save()

$ quit() or Ctrl + D
