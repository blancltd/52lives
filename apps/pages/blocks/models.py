# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from blanc_basic_assets.fields import AssetForeignKey
from blanc_pages.models.blocks import BaseBlock
from pages import choices as choices


@python_2_unicode_compatible
class Video(BaseBlock):
    thumbnail_image = AssetForeignKey('assets.Image', null=True, on_delete=models.PROTECT)
    title = models.TextField()
    video_embed_link = models.URLField(blank=True)
    colour = models.CharField(blank=True, max_length=40, choices=choices.COLOUR_CHOICES)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return 'Video'


class TwoColumnBlock(BaseBlock):
    column_one_thumbnail_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='first_image')
    column_one_title = models.TextField()
    column_one_video_embed_link = models.URLField(blank=True)
    column_one_colour = models.CharField(blank=True, max_length=40, choices=choices.COLOUR_CHOICES)

    column_two_thumbnail_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='second_image')
    column_two_title = models.TextField()
    column_two_video_embed_link = models.URLField(blank=True)
    column_two_colour = models.CharField(blank=True, max_length=40, choices=choices.COLOUR_CHOICES)

    column_ratio = models.CharField(blank=True, max_length=40, choices=choices.COLUMN_CHOICES)


class ThreeColumnImageBlock(BaseBlock):
    column_one_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='first_column_image')
    column_one_heading =  models.TextField(blank=True)
    column_two_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='second_column_image')
    column_two_heading =  models.TextField(blank=True)
    column_three_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='third_column_image')
    column_three_heading =  models.TextField(blank=True)