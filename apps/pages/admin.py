from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from blanc_pages import block_admin

from .blocks.models import Video, TwoColumnBlock, ThreeColumnImageBlock

block_admin.site.register(Video)
block_admin.site.register_block(Video, 'Advanced')

block_admin.site.register(TwoColumnBlock)
block_admin.site.register_block(TwoColumnBlock, 'Advanced')

block_admin.site.register(ThreeColumnImageBlock)
block_admin.site.register_block(ThreeColumnImageBlock, 'Advanced')