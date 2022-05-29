from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# All Django Model Field there: https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Topic(models.Model):
    """Theme which user is study e.g."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return string value of model."""
        return self.text

class Entry(models.Model):
    """Info how user is studied."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string value of model."""
        return f"{self.text[:50]}..."
