# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Nominator


@admin.register(Nominator)
class NominatorAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = (
        'first_name', 'last_name', 'reason', 'life__first_nane', 'life__last_name', 'email',
        'home_phone', 'mobile_phone',
    )
    list_display = (
        'first_name', 'last_name', 'reason', 'life', 'title', 'email', 'home_phone',
        'mobile_phone', 'hear_about_us', 'updated_at', 'created_at',
    )
    list_filter = ('reason',)
    fieldsets = (
        (
            'Nominator', {
                'fields': (
                    'title', 'first_name', 'last_name', 'life', 'reason', 'message',
                    'hear_about_us',
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
    raw_id_fields = ('life',)

    readonly_fields = ('id', 'created_at', 'updated_at',)

