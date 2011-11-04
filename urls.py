# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to


# == ADMIN ======================================== #

admin.autodiscover()


# == UTIL ======================================== #

def rut_roh(request):
  """ Simulates a server error """
  1/0
    

# == URLPATTERNS ======================================== #

urlpatterns = patterns('',
  (r'^rut-rot/$', rut_roh),
  url(r'^$', include('website.urls')),
  #url(r'^$', 'unitech.views.index', name='index'),
  
  # == admin dashboard == #
  url(r'^dashboard/', include(admin.site.urls)),
  url(r'^dashboard/doc/', include('django.contrib.admindocs.urls')),  
)


# == LOCAL ======================================== #

if settings.LOCAL_DEVELOPMENT:
  urlpatterns += patterns("django.views",
    url(r"^_assets/(?P<path>.*)", "static.serve", {
        "document_root": settings.MEDIA_ROOT,
    })
  )

