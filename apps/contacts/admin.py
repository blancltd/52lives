# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'email', 'subject', 'content', 'created_at')
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

