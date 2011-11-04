from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to

admin.autodiscover()

def rut_roh(request):
  """ Simulates a server error """
  1/0
    
urlpatterns = patterns('',
  (r'^rut-rot/$', rut_roh),
  url(r'^$', 'unitech.views.home', name='home'),
  url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
  url(r"^admin/(.*)", admin.site.root),
)

if settings.LOCAL_DEVELOPMENT:
  urlpatterns += patterns("django.views",
    url(r"^_assets/(?P<path>.*)", "static.serve", {
        "document_root": settings.MEDIA_ROOT,
    })
  )
