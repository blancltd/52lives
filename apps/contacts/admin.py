# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from blanc_pages import block_admin

from .blocks.forms import ContactFormBlock, SchoolContactFormBlock
from .models import Contact, SchoolContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'email', 'subject', 'content', 'created_at', 'id')
    fieldsets = (
        (
            'Contact', {
                'fields': (
                    'name', 'email', 'subject', 'content',
                )
            }
        ),
        (
            _('Meta data'), {
                'classes': ('collapse',),
                'fields': (
                    'id', 'created_at',
                )
            }
        ),
    )
    readonly_fields = list_display

    def has_add_permission(self, request):
        return False


@admin.register(SchoolContact)
class SchoolContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'position', 'school', 'year_group', 'created_at', 'id')
    fieldsets = (
        (
            'SchoolContact', {
                'fields': (
                    'name',
                    'position',
                    'school',
                    'address',
                    'telephone',
                    'email',
                    'year_group',
                    'workshop_date',
                    'hear_about',
                )
            }
        ),
        (
            _('Meta data'), {
                'classes': ('collapse',),
                'fields': (
                    'id', 'created_at',
                )
            }
        ),
    )
    readonly_fields = [
        'name',
        'position',
        'school',
        'address',
        'telephone',
        'email',
        'year_group',
        'workshop_date',
        'hear_about',
        'created_at',
        'id'
    ]

    def has_add_permission(self, request):
        return False


block_admin.site.register((ContactFormBlock))
block_admin.site.register_block(ContactFormBlock, 'Forms')


block_admin.site.register((SchoolContactFormBlock))
block_admin.site.register_block(SchoolContactFormBlock, 'Forms')
