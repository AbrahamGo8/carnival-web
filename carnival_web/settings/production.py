import os

from .base import *  # noqa

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carnival_db',
        'HOST': os.environ['CARNIVAL_POSTGRES_HOST'],
        'PORT': '5432',
        'USER': os.environ['CARNIVAL_POSTGRES_USERNAME'],
        'PASSWORD': os.environ['CARNIVAL_POSTGRES_PASSWORD']
    }
}
