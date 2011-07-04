from settings import *

DEBUG = True

ADMINS = []

# Disable all caching
CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_SECONDS = 1
