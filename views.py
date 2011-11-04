# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from view_utils import *
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
import logging


# == VIEWS ======================================== #

