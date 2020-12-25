""" Example of settings."""

# Default PostgreSQL and MySQL called users
DATABASES = {
        'default': {
            'NAME': 'app_data',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'postgres_user',
            'PASSWORD': 's3krit'
        },
        'users': {
            'NAME': 'user_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_user',
            'PASSWORD': 'priv4te'
        }
}

###############
# default free ant set up DATABASE_ROUTERS
DATABASES = {
        'default': {},
        'users': {
            'NAME': 'user_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_user',
            'PASSWORD': 'superS3cret'
        },
        'customers': {
            'NAME': 'customer_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_cust',
            'PASSWORD': 'veryPriv@te'
        }
}

#############

