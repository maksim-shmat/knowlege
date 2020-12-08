""" signals.py, apps.py, settings.py

Signals realization in three files.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from . import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.Profile(user=instance)
    profile.save()

###############
# apps.py
from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    name = "profiles"
    verbose_name = 'User Profiles'

    def ready(self):
        from . import signals

###############
INSTALLED_APPS = [
        'profiles.apps.ProfilesConfig',
        'posts',
        ...

