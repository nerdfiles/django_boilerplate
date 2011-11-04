# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.core.urlresolvers import reverse
from django import http
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import loader, Context
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView
from sekizai.context import SekizaiContext


# == UTIL ======================================== #

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)
    
def server_error(request, template_name='500.html'):
  t = loader.get_template(template_name) # You need to create a 500.html template.
  return http.HttpResponseServerError(t.render(Context({
      "MEDIA_URL": settings.MEDIA_URL
  })))


# == VIEWS ======================================== #

