from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from cms_taggit import models


class PageTaggitAdmin(admin.StackedInline):
    """Inline admin interface for `PageTaggit` model."""

    model = models.PageTaggit

PageAdmin.inlines.append(PageTaggitAdmin)
 
admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)

