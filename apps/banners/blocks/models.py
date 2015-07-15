# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from blanc_basic_assets.fields import AssetForeignKey
from blanc_pages.models.blocks import BaseBlock


@python_2_unicode_compatible
class Banner(BaseBlock):
    image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT)
    content = models.TextField()
    link = models.URLField(blank=True)
    link_text = models.CharField(blank=True, max_length=40)

    class Meta:
        ordering = ('link',)

    def __str__(self):
        return 'Banner'

