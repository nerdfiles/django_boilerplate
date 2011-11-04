# -*- coding: utf-8 -*-

# == ALBUM ======================================= #

"""
  Can - Future Days
  http://open.spotify.com/track/742Qq4oImak5UxgZu25897
"""

# == PROJECT ======================================= #

"""
  @project          django_boilerplate
  @contributor      Aaron Alexander (nerdfiles@gmail.com)
  @datetime         11.4.2011.11.56.a
  @devlogin         admin/admin
"""

# == IMPORTS ======================================= #

from django.conf import settings
import os, sys, datetime
import logging


# == UTIL ======================================= #

PROJECT_ROOT = os.path.dirname(__file__)
DIRNAME = os.path.dirname(os.path.abspath(__file__))

# == pythonpath inserts == #

# local
 
#sys.path.insert(0, PROJECT_ROOT)
#sys.path.insert(1, os.path.join(PROJECT_ROOT, "djangologging"))

# apache mod_wsgi

#sys.path.append(PROJECT_ROOT)
#sys.path.append(os.path.join(PROJECT_ROOT, "djangologging"))


# == VENV ======================================== #

VENV_ROOT = os.path.join('/Users','pbdigital','.virtualenvs','django_boilerplate')


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

SECRET_KEY = 'h35nfv4bn6klt-1@dkyknvc*-h@$n7fm92$^9kc6^^6ito*jd4'


# == DB ======================================= #

"""
  @engines 'postgresql_psycopg2'|'postgresql'|'mysql'|'sqlite3'|'oracle'
  @note If using local settings, this will be overridden.
"""

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''


# == LANGUAGE ======================================= #

LANGUAGE_CODE = 'en-us'


# == I18N ======================================= #

USE_I18N = True


# == LOCALIZATION ======================================= #

USE_L10N = True


# == URLCONF ======================================= #

ROOT_URLCONF = 'django_boilerplate.urls'


# == URL ======================================= #

# == media url == #

MEDIA_URL = '/_assets/'

# == admin media == #

ADMIN_MEDIA_PREFIX = '/_assets/admin/'


# == THEME/TEMPLATE/MEDIA ======================================= #

# == theme == #

THEME = "boilerplate"
THEME_DIR = os.path.join(PROJECT_ROOT, "_themes", THEME)

# == template == #

TEMPLATE_DIRS = (
  #os.path.join(PROJECT_ROOT, "_themes",),
  os.path.join(PROJECT_ROOT, "_themes", THEME, "_templates"),
)

# == media == #

MEDIA_ROOT = os.path.realpath(os.path.join(THEME_DIR, "_assets"))


# == STATIC ======================================= #
"""
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
"""

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
  
  'debug_toolbar.middleware.DebugToolbarMiddleware',
  
  #'djangologging.middleware.LoggingMiddleware',
  #'djangologging.middleware.SuppressLoggingOnAjaxRequestsMiddleware',
)


# == INSTALLED APPS ======================================= #

INSTALLED_APPS = (

  # == core == #
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  
  # == apps == #
  'debug_toolbar',
  'south',
  
  # == custom/django_boilerplate == #
  
  'django_boilerplate',
  
  # == admin == #
  'django.contrib.admin',
  'django.contrib.admindocs',
)


# == APP: DEBUG TOOLBAR ======================================= #
"""
  @see http://pypi.python.org/pypi/django-debug-toolbar/
"""

DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.version.VersionDebugPanel',
  'debug_toolbar.panels.timer.TimerDebugPanel',
  'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
  'debug_toolbar.panels.headers.HeaderDebugPanel',
  'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
  'debug_toolbar.panels.template.TemplateDebugPanel',
  'debug_toolbar.panels.sql.SQLDebugPanel',
  'debug_toolbar.panels.signals.SignalDebugPanel',
  'debug_toolbar.panels.logger.LoggingPanel',
)

def custom_show_toolbar(request):
  return True

DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
  'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}


# == APP: PIL ======================================= #
"""
  @see http://www.pythonware.com/products/pil/
"""

PIL_IMAGEFILE_MAXBLOCK = 1024 * 2 ** 10


# == EMAIL SETTINGS ======================================= #

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# == LOGGING ======================================= #

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    },
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'file': {
      'level': 'INFO',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': os.path.join(PROJECT_ROOT, '_log', 'requests.log'),
      'maxBytes': 1024*1024*5, # 5MB
      'backupCount': 10,
      'formatter': 'standard'
    },
    'file_userlogins': {              # define and name a handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, '_log', 'userlogins.log') # log file
    },
    'file_usersaves': {               # define and name a second handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, '_log', 'usersaves.log')  # log file
    },
  },
  'loggers': {
    'django.request': {
      'handlers': ['file'],
      'level': 'INFO',
      'propagate': False,
    },
    'logview.userlogins': {            # define a logger - give it a name
      'handlers': ['file_userlogins'], # specify what handler to associate
      'level': 'INFO',                 # specify the logging level
      'propagate': True,
    },     

    'logview.usersaves': {             # define another logger
      'handlers': ['file_usersaves'],  # associate a different handler
      'level': 'INFO',                 # specify the logging level
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


# == LOCAL ======================================= #

try:
  from local_settings import *
except ImportError:
  pass

