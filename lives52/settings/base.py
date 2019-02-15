# -*- coding: utf-8 -*-

"""
Django settings for lives52 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import sys
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Production / development switches
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')

SECRET_KEY = os.environ.get('SECRET_KEY')


# Email
# https://docs.djangoproject.com/en/1.8/ref/settings/#email

ADMINS = (
    ('Developer Society', 'studio@dev.ngo'),
)

MANAGERS = ADMINS

SERVER_EMAIL = 'lives52@devsoc.org'

DEFAULT_FROM_EMAIL = 'lives52@devsoc.org'

EMAIL_SUBJECT_PREFIX = '[lives52] '


# PROJECT ROOT APPS
PROJECT_APPS_ROOT = os.path.join(BASE_DIR, 'apps')
sys.path.append(PROJECT_APPS_ROOT)


# Application definition
DEFAULT_APPS = [
    'blanc_admin_theme',  # must be before django.contrib.admin
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'blanc_basic_assets',
    'blanc_basic_news',
    'blanc_pages',
    'blanc_pages_form_block',
    'blanc_pages_image_block',
    'blanc_pages_redactor_block',
    'captcha',
    'django_mptt_admin',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'mptt',
    'raven.contrib.django.raven_compat',
    'redactorjs_staticfiles',
    'sorl.thumbnail',
    'two_factor',
]


PROJECT_APPS = [
    'addresses',
    'banners',
    'companies',
    'contacts',
    'countries',
    'lives',
    'notes',
    'pages',
    'people',
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS


MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blanc_pages.middleware.BlancpageFallbackMiddleware',
]

ROOT_URLCONF = 'lives52.urls'

WSGI_APPLICATION = 'lives52.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}


# Caches
# https://docs.djangoproject.com/en/1.8/topics/cache/

CACHES = {}
if os.environ.get('MEMCACHED_SERVERS'):
    CACHES['default'] = {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': os.environ['MEMCACHED_SERVERS'].split(' '),
        'KEY_PREFIX': os.environ.get('MEMCACHED_PREFIX'),
    }
else:
    CACHES['default'] = {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'


# Datetime config.
DATE_FORMAT = 'd M Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'd M Y H:i'


TIME_ZONE = 'Europe/London'


USE_I18N = True

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs/static')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# File uploads
# https://docs.djangoproject.com/en/1.8/ref/settings/#file-uploads

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs/media')

DEFAULT_FILE_STORAGE = os.environ.get(
    'DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage'
)


# Templates
# https://docs.djangoproject.com/en/1.8/ref/settings/#templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}


# Any other application config goes below here

# 2FA login url
LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'admin:index'

# Sites framework
SITE_ID = 1

# Cloud storage
CONTENTFILES_PREFIX = '52lives'
CONTENTFILES_SSL = True

# Blanc Pages
BLANC_PAGES_MODEL = 'pages.Page'
BLANC_PAGES_DEFAULT_TEMPLATE = 'blanc_pages/default.html'
BLANC_PAGES_DEFAULT_BLOCKS = (
    ('blanc_pages_redactor_block.RedactorBlock', 'Text'),
    ('blanc_pages_image_block.ImageBlock', 'Image'),
    ('pages.HTML', 'HTML'),
)

# Thumbnail generation
THUMBNAIL_PREFIX = 'thumbs/'
THUMBNAIL_PRESERVE_FORMAT = True
THUMBNAIL_QUALITY = 100

# Recaptcha
if 'RECAPTCHA_PUBLIC_KEY' in os.environ:
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
NOCAPTCHA = True
