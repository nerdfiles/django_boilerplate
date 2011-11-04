# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf.urls.defaults import *


# == URLPATTERNS ======================================== #

urlpatterns = patterns('',
  url(r'^$', 'website.views.index', name='index'),
)

