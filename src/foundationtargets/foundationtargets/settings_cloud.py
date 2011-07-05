from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'foundationtargets', # Or path to database file if using sqlite3.
        'USER': 'foundationtargets', # Not used with sqlite3.
        'PASSWORD': 'foundationtargets', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += ('gunicorn',)
