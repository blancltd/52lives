# -*- coding: utf-8 -*-

from blanc_pages import block_admin

from .blocks.models import Banner


block_admin.site.register(Banner)
block_admin.site.register_block(Banner, 'Banners')

