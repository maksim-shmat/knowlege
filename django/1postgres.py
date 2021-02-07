"""About PostgreSQL with Django."""

# postgreSQL specific db constraints
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.field import DateTimeRangeField, RangeOperators
from django.db import models
from django.db.models import Q

class Room(models.Model):
    number = models.IntegerField()


class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    timespan = DateTimeRangeField()
    cancelled = models.BooleanField(default=False)

    
    class Meta:
        constraints = [
                ExclusionConstraint(
                    name='exclude_overlapping_reservations',
                    expressions=[
                        ('timespan', RangeOperators.OVERLAPS),
                        ('room', RangeOperators.EQUAL),
                    ],
                    condition=Q(cancelled=False),
                ),
        ]

############## case using two fields
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.field import (
        DateTimeRangeField,
        RangeBoundary,
        RangeOperators,
)
from django.db import models
from django.db.models import Func, Q


class TsTzRange(Func):
    function = 'TSTZRANGE'
    output_field = DateTimeRangeField()


class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    cancelled = models.BooleanField(default=False)

    
    class Meta:
        constraints = [
                ExclusionConstraint(
                    name='exclude_overlapping_reservations',
                    expressions=(
                        (TsTzRange('start', 'end', RangeBoundary()),
                            RangeOperators.OVERLAPS),
                        ('room', RangeOperators.EQUAL),
                    ),
                    condition=Q(cancelled=False),
                ),
        ]

############# subclassing the built-in database backend
# mysite/mydbengine/base.py
from django.db.backends.postgresql import base, features

class DatabaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True


class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures

### DATABASE-ENGINE in your settings.py file
DATABASES = {
        'default': {
            'ENGINE': 'mydbengine',
            ...
        },
}

########### migration operations
# RunPython
from django.db import migrations

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).bulk_create([
        Country(name="USA", code="us"),
        Country(name="France", code="fr"),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).filter(name="USA", code="us").delete()
    Country.objects.using(db_alias).filter(name="France", code="fr").delete()


class Migration(migrations.Migration):
    dependencies = []
    operations = [
            migrations.RunPython(forwards_func, reverse_func),
    ]

############
