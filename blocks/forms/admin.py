# -*- coding: utf-8 -*-

from blanc_pages import block_admin

from .forms import ContactFormBlock, NominateFormBlock

block_admin.site.register((ContactFormBlock, NominateFormBlock))
block_admin.site.register_block(ContactFormBlock, 'Forms')
block_admin.site.register_block(NominateFormBlock, 'Forms')

