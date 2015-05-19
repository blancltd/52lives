# -*- coding: utf-8 -*-

import os

from .base import *  # NOQA @UnusedWildImport


DEBUG = True

TEMPLATE_DEBUG = DEBUG

THUMBNAIL_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME'),
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
    },
}

INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS.append(
    'debug_toolbar',
)

MIDDLEWARE_CLASSES.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

COVERAGE_EXCLUDES_FOLDERS = ['/var/envs/lives52/lib/python2']

SECRET_KEY = "lives52"

