"""Management in Django."""

#1 Create required folders

mkdir app_name/management app_name/mangement/commands && cd $_

#2 Create a python file with your command name

touch your_command_name.py

#3 Edit your new python file, start with import

from django.core.management.base import BaseCommand
## import anything else 

#4 Create the Command class that will handle your command

class Command(BaseCommand):
    help = "This message will be shon with the --help option after your command"
    def handle(self, args, *kwargs):
        # Work the command is supposed to do

#5 And this is now you execute your custom command

python manage.py my_custom_command
