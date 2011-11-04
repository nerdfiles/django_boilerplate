from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pagemodel import Page
from taggit.managers import TaggableManager


class PageTaggit(models.Model):
    """Model for `django-taggit` and additional meta data integration with Django CMS."""

    page = models.ForeignKey(Page, verbose_name=_('Page'), unique=True,
        editable=False)
    meta_description = models.CharField(_('Description meta tag'), blank=True,
        max_length=255,
        help_text='A description of the page sometimes used by search engines.')
    tags = TaggableManager(verbose_name=_('Tags'), blank=True)

    class Meta:
        verbose_name = _('Page Taggit')
        verbose_name_plural = _('Page Taggits')

    def __unicode__(self):
        return u'Page Taggit for {0}'.format(self.page)

