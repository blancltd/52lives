# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.utils import unquote
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from blanc_pages import block_admin

from addresses.admin import AddressInline
from notes.admin import NoteInline

from .blocks.forms import NominateFormBlock
from .models import Person, Nominator, Nominee


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline, NoteInline
    ]
    date_hierarchy = 'created_at'
    search_fields = (
        'first_name', 'last_name', 'life__first_name', 'life__last_name', 'email',
        'home_phone', 'mobile_phone',
    )
    list_display = (
        'first_name', 'last_name', 'reason', 'life', 'title', 'email', 'home_phone',
        'mobile_phone', 'hear_about_us', 'updated_at', 'created_at',
    )
    list_filter = ('reason',)
    fieldsets = (
        (
            'Person', {
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
        urls = super(PersonAdmin, self).get_urls()
        extra_urls = [
            url(
                r'^(\d+)/add-note/$',
                self.add_note,
                name='persons-add-note'
            ),
            url(
                r'^(\d+)/add-address/$',
                self.add_address,
                name='persons-add-address'
            )
        ]
        return extra_urls + urls

    def get_inline_instances(self, request, obj=None):
        """ Update post url for AddressInline and NotesInline. """
        inline_instances = super(PersonAdmin, self).get_inline_instances(request, obj)
        if obj is not None:
            for inline in inline_instances:
                if isinstance(inline, AddressInline):
                    inline.dialog_data['post_url'] = reverse(
                        'admin:persons-add-address', args=(obj.id,)
                    )
                elif isinstance(inline, NoteInline):
                    inline.dialog_data['post_url'] = reverse(
                        'admin:persons-add-note', args=(obj.id,)
                    )
        return inline_instances

    def get_formsets_with_inlines(self, request, obj=None):
        if obj is None:
            return []
        return super(PersonAdmin, self).get_formsets_with_inlines(request, obj)

    def add_note(self, request, object_id):
        """ Add note for life. """
        context = {}
        obj = self.get_object(request, unquote(object_id))
        context = NoteInline.create_note(
            request, obj
        )
        return JsonResponse(context)

    def add_address(self, request, object_id):
        """ Add address for person. """
        obj = self.get_object(request, unquote(object_id))
        context = AddressInline.create_address(
            request, obj
        )

        return JsonResponse(context)


class NomineeInline(admin.StackedInline):
    model = Nominee
    max_num = 1
    readonly_fields = (
        'first_name', 'last_name', 'email', 'phone', 'relation', 'why_help', 'what_need',
        'get_html_address',
    )


@admin.register(Nominator)
class Nominator(PersonAdmin):
    list_filter = ()
    inlines = [
        NomineeInline, AddressInline, NoteInline
    ]
    fieldsets = (
        (
            'Person', {
                'fields': (
                    'title', 'first_name', 'last_name', 'life', 'hear_about_us',
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


block_admin.site.register((NominateFormBlock))
block_admin.site.register_block(NominateFormBlock, 'Forms')
