#!/usr/bin/env python

# == IMPORTS ======================================== #

from django.conf import settings


# == CONTEXT PROCESSORS ======================================== #

def google_analytics(request):

    if not settings.GA_PATH:
        return {}

    f = None
    try:
        f = file(settings.GA_PATH)
        GA_CODE = f.read()
    finally:
        if f is not None:
            f.close()

    return dict(GA_CODE=GA_CODE)

