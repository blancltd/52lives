# -*- coding: utf-8 -*-

from .base import *  # NOQA @UnusedWildImport


DEBUG = False

TEMPLATE_DEBUG = DEBUG

# Cache sessions for optimum performance
if os.environ.get('REDIS_SERVERS'):
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
