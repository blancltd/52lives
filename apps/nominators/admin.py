# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.utils import unquote
from django.http import JsonResponse

from addresses.admin import AddressInline

from .models import Nominator


@admin.register(Nominator)
class NominatorAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
    ]
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
            'Contacts', {
                'classes': ('collapse',),
                'fields': (
                    'email', 'home_phone', 'mobile_phone',
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

    class Media:
        js = ('js/admin/addresses/addresses.js',)

    def get_urls(self):
        urls = super(NominatorAdmin, self).get_urls()
        life_urls = [
            url(
                r'^(\d+)/add-address/$',
                self.add_address,
                name='nominators-add-address'
            )
        ]
        return life_urls + urls

    def get_formsets_with_inlines(self, request, obj=None):
        if obj is None:
            return []
        return super(NominatorAdmin, self).get_formsets_with_inlines(request, obj)

    def add_address(self, request, object_id):
        """ Add address for nominator. """
        obj = self.get_object(request, unquote(object_id))
        context = AddressInline.create_address(
            request, obj
        )

        return JsonResponse(context)

