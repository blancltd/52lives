# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from blanc_basic_assets.fields import AssetForeignKey
from blanc_pages.models.blocks import BaseBlock
from pages import choices as colour_choices


@python_2_unicode_compatible
class Video(BaseBlock):
    thumbnail_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT)
    title = models.TextField()
    video_embed_link = models.URLField(blank=True)
    colour = models.CharField(blank=True, max_length=40, choices=colour_choices.COLOUR_CHOICES)


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return 'Video'

