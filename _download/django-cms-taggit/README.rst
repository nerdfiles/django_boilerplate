===================
 django-cms-taggit
===================

Integration of the ``django-taggit`` application and also some additional meta
data with `Django CMS <http://www.django-cms.org/>`_.

``django-taggit`` a better and simpler approach to tagging with Django and with
this you can comfortable use it with `Django CMS`.

Requirements
============

- django
- django-cms
- django-taggit

Installation
============

Using PyPI you can simply type into a terminal:

    pip install django-cms-taggit

or

    easy_install django-cms-taggit

Setup
=====

In your ``settings.py`` file add ``cms_taggit`` to the list of
``INSTALLED_APPS``. Don't forget to syncdb your database or migrate if you're
using ``south``.

Because some HTML meta tags (keywords, description) can be implemented with this
(see ``templates`` folder) it is recommended to turn off the `Django CMS`
setting ``CMS_SEO_FIELDS``.

Author
======

Copyright 2011 GW <gw.2011@tnode.com or http://gw.tnode.com/>

Released under GPLv3 or newer.

