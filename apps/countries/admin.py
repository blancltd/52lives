# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'iso_3166_1_a2',
    )
    search_fields = (
        'name',
    )

    fieldsets = (
        (
            'Country', {
                'fields': (
                    'name', 'iso_3166_1_a2',
                )
            }
        ),
        (
            'Meta data', {
                'classes': ('collapse',),
                'fields': (
                    'id',
                )
            }
        ),
    )

    readonly_fields = ('id',)


