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
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

#########
# add poll Date information
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,                {'fields': ['question_text']}),
            ('Date information',  {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

############
# add 3 choices
from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline): # or (admin.TabularInline): for table
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,                 {'fields': ['question_text']}),
            ('Date information',   {'fields': ['pub_date'], 'clsses': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

##########
# add subnames in head string
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')

#######
# add bool mark and sort filter, and search
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    list_filter = ['pub_date']  # is may this place?
    search_fields = ['question_text']  # and this there?

#########


