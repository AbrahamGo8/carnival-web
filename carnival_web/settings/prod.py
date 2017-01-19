from carnival_web.settings import base

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carnival_db',
        'HOST': '',
        'PORT': '5432',
        'USER': '',
        'PASSWORD': '',
    }
}