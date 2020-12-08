""" Services.py for business logic, right? """

# this not good
class Profile(models.Model):
    ...
    def is_superhero(self):
        url = "http://api.herocheck.com/?q={0}".format(
                self.user.username)
        return webclient.get(url)

###################
# do that
from .srvices import SuperHeroWebAPI

class Profile(models.Model):
    def is_superhero(self):
        return SuperHeroWebAPI.is_hero(self.user.username)

# and add this to file: services.py
class SuperHeroWebAPI:
    ...
    @staticmethod
    def is_hero(username):
        url = API_URL.format(username)
        return webclient.get(url)

# And now add anything to blacklist... easy
class SuperHeroWebAPI:
    ...j
    @staticmethod
    def is_hero(username):
        blacklist = set(["syndrome", "kcka$$", "superfake"])
        url = API_URL.format(username)
        return username not in blacklist and webclient.get(url)
