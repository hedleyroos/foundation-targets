from settings import *

DEBUG = True

# Disable all caching
CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_SECONDS = 1
