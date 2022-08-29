from os import environ

from .base import *


DEBUG = False

SECRET_KEY = environ["SECRET_KEY"]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ["url-storage-revitalyze.herokuapp.com"]
