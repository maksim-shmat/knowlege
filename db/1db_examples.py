""" Postgres with Django."""

###### Controlling Database Behavior

class DurationField(models.Field):
    def db_type(self, connection):
        engine = connection.settings_dect['ENGINE']
    if  engine == 'django.db.backends.postgresql_psycopg2':
        return 'interval'
    else:
        return connection.creation.data_types['DecimalField']


###### get_prep_value(self,value)

from django.db import models
from django.db.models.fields.subclassing import SubfieldBase
from django.utils import _decimal

class DurationField(models.DecimalField, metaclass=SubfieldBase):
    def get_prep_value(self, value):
        return _decimal.Decimal('%s.%s' % (value.days * 86400 + value.seconds,
                                           value.microseconds))
    # Field logic then continues here

###### get_db_prep_value(self, value, connection, perpared=False)

from django.db import models
from django.db.models.fields.subclassing import SubfieldBase
from django.utils import _decimal

class DurationField(models.DecimalField, metaclass=SubfieldBase):
    def get_prep_value(self, value):
        # Nothing to do here, because get_db_prep_value() will do the dirty work
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        engine = connection.settings_dict['ENGINE']
        if engine == 'django.db.backends.postgresql_psycopg2':
            # PostgreSQL can handle timedeltas directly
            return value
        else:
            return _decimal.Decimal('%s.%s' % (value.days * 86400 + value.seconds,
                                               value.microseconds))
    # Field logic then continue here

######
