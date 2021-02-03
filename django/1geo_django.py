"""Geographic Models."""

# Defining a Geographic Model
from .contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntergerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

########### LayerMapping
# create a file called load.py inside the world application
from pathlib import Path
from django.contrib.gis.utils import LayerMapping

world_mapping = {
        'fips': 'FIPS',
        'iso2': 'ISO2',
        'iso3': 'ISO3',
        'un': 'UN',
        'name': 'NAME',
        'area': 'AREA',
        'pop2005': 'POP2005',
        'region': 'REGION',
        'subregion': 'SUBREGION',
        'lon': 'LON',
        'lat': 'LAT',
        'mpoly': 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'TM_WORLD_BORDERS-0.3.shp'
def run(verbose=True):
    lm = LayerMapping(WorldBorder, str(world_shp), world_mapping,
            transform=False)
    lm.save(strict=True, verbose=verbose)

############# automate LayerMapping with the orginspect
# this is an auto-generated Django model module crated by ogrinspect.
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.CharField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

# auto-generated 'LayerMapping' dictionary for WorldBorder model
worldborders_mapping = {
        'fips': 'FIPS',
        'iso2': 'ISO2',
        'iso3': 'ISO3',
        'un': 'UN',
        'name': 'NAME',
        'area': 'AREA',
        'pop2005': 'POP2005',
        'region': 'REGION',
        'subregion': 'SUBREGION',
        'lon': 'LAT',
        'geom': 'MULTIPOLYGON',
}

############## raw queries
from django.db import connection
# or if you're querying a non-default database:
from django.db import connections
connection = connections['your_gis_db_alias']

City.objects.raw('SELECT id, name, %s as point from myapp_city' %
        (connection.ops.select % 'point'))

##############


