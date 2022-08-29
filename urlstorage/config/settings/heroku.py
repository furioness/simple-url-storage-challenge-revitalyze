from os import environ

import dj_database_url

from .base import *


DEBUG = False

SECRET_KEY = environ["SECRET_KEY"]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ["url-storage-revitalyze.herokuapp.com"]

DATABASES["default"] = dj_database_url.config(  # type: ignore[assignment]
    default=environ["DATABASE_URL"]
)
