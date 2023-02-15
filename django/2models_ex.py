"""more Django models examples."""

#1 For beter readability in admin display the headline for each note

from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.headline  # This


#2
