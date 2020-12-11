""" Admin site is began of this. """

class SightingAdmin(admin.ModelAdmin):
    list_display = ('superhero', 'power', 'location', 'sighted_on')
    date_hierarchy = 'sighted_on'
    search_fields = ['superhero']
    ordering = ['superhero']

admin.site.register(models.Sighting, SightingAdmin)

################
from django.contrib import admin
from .models import Question

admin.site.register(Question)    # And first write class Question in views.py
################

