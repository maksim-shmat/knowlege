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

##############
