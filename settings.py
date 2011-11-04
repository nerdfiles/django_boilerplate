# == ALBUM ======================================= #

"""
  Can - Future Days
  http://open.spotify.com/track/742Qq4oImak5UxgZu25897
"""

# == PROJECT ======================================= #

"""
  @project          unitech
  @contributor      Aaron Alexander (nerdfiles@gmail.com)
  @contributor      Will Dawson (will@pennebaker.com)
  @datetime         11.4.2011.11.56.a
"""

# == IMPORTS ======================================= #

import os, sys, datetime


# == UTIL ======================================= #

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
DIRNAME = os.path.dirname(os.path.abspath(__file__))


# == DEVELOPMENT/DEBUGGING ======================================= #

LOCAL_DEVELOPMENT = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG


# == ADMIN/GENERAL ======================================= #

ADMINS = (
  ('nerdfiles', 'nerdfiles@gmail.com'),
  ('Richard', 'richard@pennebaker.com'),
  ('Will', 'will@pennebaker.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)


# == DB ======================================= #

"""
  @note If using local settings, this will be overridden.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# == LANGUAGE ======================================= #

LANGUAGE_CODE = 'en-us'


# == I18N ======================================= #

USE_I18N = True


# == LOCALIZATION ======================================= #

USE_L10N = True


# == THEME ======================================= #

THEME = "unitech"
THEME_DIR = os.path.join(PROJECT_ROOT, "_themes", THEME)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "_themes", THEME, "templates"),
)
MEDIA_ROOT = os.path.realpath(os.path.join(THEME_DIR, "_assets"))


# == URL ======================================= #

MEDIA_URL = '/_assets/'


# == ADMIN ======================================= #

ADMIN_MEDIA_PREFIX = '/_assets/admin/'


# == STATIC ======================================= #

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SECRET_KEY = 'h35nfv4bn6klt-1@dkyknvc*-h@$n7fm92$^9kc6^^6ito*jd4'


# == TEMPLATE LOADERS ======================================= #

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'django.template.loaders.eggs.Loader',
)


# == MIDDLEWARE CLASSES ======================================= #

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


# == URLCONF ======================================= #

ROOT_URLCONF = 'unitech.urls'


# == TEMPLATE ======================================= #

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# == INSTALLED APPS ======================================= #

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


# == LOGGING ======================================= #

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# == CACHING ======================================= #

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_TIMEOUT = 60*30
CACHE_PREFIX = "Z"


# == APP: PIL ======================================= #

PIL_IMAGEFILE_MAXBLOCK = 1024 * 2 ** 10


# == APP?: DJANGO-EMAIL ======================================= #

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# == LOCAL ======================================= #

try:
    from local_settings import *
except ImportError:
    pass

