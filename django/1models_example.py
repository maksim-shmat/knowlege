""" Examples how write models. """

class Sighting(models.Model):
    superhero = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    power = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sighted_on = models.DateTimeField()

    def __str__(self):
        return "{}'s power {} sighted at: {} on {}".format(
                self.superhero,
                self.power,
                self.location.country,
                self.sighted_on)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sighting_details', kwargs={'pk': self.id})

    class Meta:
        unique_together = ("superhero", "power")
        ordering = ["-sighted_on"]
        verbose_name = "Sighting & Encounter"
        verbose_name_plural = "Sightings & Encounters"

#############
# This example from django site, it is site-anketa.
from django.db import models

class Question(models.Model):
    """ Make a field for ask a question. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -
    datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """ Make a field for get answer. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

##########
# after tests he talk change it
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
##########

