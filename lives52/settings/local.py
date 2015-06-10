# -*- coding: utf-8 -*-

import os

from django.utils.importlib import import_module

from .base import *  # NOQA @UnusedWildImport


DEBUG = True

THUMBNAIL_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'first_man_standing'),
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
    },
}

INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]


try:
    import_module('flat')
except ImportError:
    pass
else:
    INSTALLED_APPS.insert(0, 'flat')


MIDDLEWARE_CLASSES.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

COVERAGE_EXCLUDES_FOLDERS = ['/var/envs/first_man_standing/lib/python2']

SECRET_KEY = "first_man_standing"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

