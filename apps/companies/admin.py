# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Company, Life


class LifeInline(admin.TabularInline):
    model = Life
    readonly_fields = (
        'title', 'is_published', 'first_name', 'last_name', 'number', 'image', 'email',
        'home_phone', 'mobile_phone', 'request_title', 'content', 'request', 'summary',
        'thank_you', 'slug', 'created_at',
    )
    max_num = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (LifeInline,)
    list_display = ('title', 'description', 'image',)
    search_fields = ['title', 'description']
    readonly_fields = ('id',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (
            'Company', {
                'fields': (
                    'title', 'description', 'image', 'slug',
                )
            }
        ),
        (
            'Meta', {
                'classes': ('collapse',),
                'fields': (
                    'id',
                )
            }
        ),
    )


@admin.register(Life)
class LifeAdmin(admin.ModelAdmin):
    list_display = (
        'get_full_name', 'is_published', 'company', 'number', 'request_title', 'home_phone',
        'mobile_phone', 'created_at', 'updated_at',
    )
    list_filter = ('company', 'is_published',)
    readonly_fields = ('id', 'updated_at')
    search_fields = ['company__title', 'first_name', 'last_name', 'email']
    fieldsets = (
        (
            'Live', {
                'fields': (
                    'company', 'title', 'first_name', 'last_name', 'number',
                    'image', 'is_published',
                )
            }
        ),
        (
            'About', {
                'fields': (
                    'request_title', 'content', 'request',
                )
            }
        ),
        (
            'Contacts', {
                'classes': ('collapse',),
                'fields': (
                    'email', 'home_phone', 'mobile_phone',
                )
            }
        ),

        (
            'Approved information', {
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
