""" Пример установки данных в таблицы с помощью Django. """

class Origin(models.Model):
    superhero = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return "{}'s origin: {}".format(self.superhero, self.origin)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return "{}: ({}, {})".format(self.country,
                                     self.latitude, self.longitude)

    class Meta:
        unique_together = ("latitude", "longitude")


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

    class Meta:
        unique_together = ("superhero", "power")

##############################################
class Postable(model.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=500)

    class Meta:
        abstract = True  # make abstract class

class Post(Postable):
    ...

class Comment(Postable):
    ...

class TimeStampedModel(model.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Postable(TimeStampedModel):   # and this mixin from TimeStamped
    message = models.TextField(max_length=500)
    ...
    class Meta:
        abstract =True

class Post(Postable):
    ...

class Comment(Postable):

##################################################
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True) # for Postgre recomend True

