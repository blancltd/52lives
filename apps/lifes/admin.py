# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Life


@admin.register(Life)
class LifeAdmin(AdminImageMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'number', 'request',)
    list_display = (
        'get_full_name', 'number', 'request', 'is_published', 'created_at', 'updated_at',
    )
    list_filter = ('is_published',)
    fieldsets = (
        (
            'Life', {
                'fields': (
                    'title', 'first_name', 'last_name', 'number',
                    'image', 'content', 'request', 'is_published',
                )
            }
        ),
        (
            'Approved information', {
                'classes': ('collapse',),
                'fields': (
                    'summary', 'thank_you',
                )
            }
        ),
        (
            'Meta data', {
                'classes': ('collapse',),
                'fields': (
                    'id', 'created_at', 'updated_at',
                )
            }
        ),
    )

    readonly_fields = ('id', 'created_at', 'updated_at', 'number',)

