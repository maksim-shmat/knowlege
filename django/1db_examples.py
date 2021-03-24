""" Postgres with Django."""

###### Controlling Database Behavior

class DurationField(models.Field):
    def db_type(self, connection):
        engine = connection.settings_dect['ENGINE']
    if  engine == 'django.db.backends.postgresql_psycopg2':
        return 'interval'
    else:
        return connection.creation.data_types['DecimalField']


######
