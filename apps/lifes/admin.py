# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.utils import unquote
from django.contrib.contenttypes.admin import GenericTabularInline
from django.http import JsonResponse

from sorl.thumbnail.admin import AdminImageMixin

from addresses.forms import AddressForm
from addresses.models import Address
from notes.forms import NoteForm
from notes.models import Note

from .models import Life


class AddressInline(GenericTabularInline):
    template = 'admin/lifes/life/edit_inlines/addresses.html'
    model = Address
    extra = 0
    min_num = 0
    can_delete = True
    list_per_page = 2
    fieldsets = (
        (
            'Notes', {
                'classes': ('collapse',),
                'fields': (
                    'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
                    'created_by', 'created_at', 'updated_at',
                )
            }
        ),
    )
    readonly_fields = (
        'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
        'created_by', 'created_at', 'updated_at',
    )


class NoteInline(GenericTabularInline):
    template = 'admin/lifes/life/edit_inlines/notes.html'
    model = Note
    extra = 0
    min_num = 0
    can_delete = True
    list_per_page = 2
    fieldsets = (
        (
            'Notes', {
                'classes': ('collapse',),
                'fields': (
                    'note', 'created_by', 'created_at', 'updated_at',
                )
            }
        ),
    )
    readonly_fields = ('note', 'created_by', 'created_at', 'updated_at',)


@admin.register(Life)
class LifeAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [
        AddressInline, NoteInline
    ]
    list_per_page = 2
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'number', 'request',)
    list_display = (
        'get_full_name', 'number', 'request', 'home_phone', 'mobile_phone', 'is_published',
        'created_at', 'updated_at',
    )
    list_filter = ('is_published',)
    fieldsets = (
        (
            'Life', {
                'fields': (
                    'title', 'first_name', 'last_name', 'number',
                    'image', 'is_published',
                )
            }
        ),
        (
            'About', {
                'classes': ('collapse',),
                'fields': (
                    'content', 'request',
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

    def get_urls(self):
        urls = super(LifeAdmin, self).get_urls()
        life_urls = [
            url(
                r'^(\d+)/add-note/$',
                self.add_note,
                name='life-add-note'
            ),
            url(
                r'^(\d+)/add-address/$',
                self.add_address,
                name='life-add-address'
            )
        ]
        return life_urls + urls

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ Add extra context in template. """
        add_note_form = NoteForm()
        add_address_form = AddressForm()
        context = {
            'add_note_form': add_note_form,
            'add_address_form': add_address_form,
        }
        if extra_context:
            context.update(extra_context)
        return super(LifeAdmin, self).change_view(
            request, object_id, form_url, extra_context=context
        )

    def add_note(self, request, object_id):
        """ Add note for life. """
        context = {}
        obj = self.get_object(request, unquote(object_id))
        add_note_form = NoteForm(request.POST)
        if add_note_form.is_valid():
            note = add_note_form.save(commit=False)
            note.content_object = obj
            note.created_by = request.user
            note.save()
            messages.success(request, 'The note "{}" was added successfully.'.format(
                note.note
            ))
            context.update({'success': True})
        else:
            context.update(add_note_form.errors)
        return JsonResponse(context)

    def add_address(self, request, object_id):
        """ Add address for life. """
        context = {}
        obj = self.get_object(request, unquote(object_id))
        add_address_form = AddressForm(request.POST)
        if add_address_form.is_valid():
            address = add_address_form.save(commit=False)
            address.content_object = obj
            address.created_by = request.user
            address.save()
            messages.success(request, 'The address "{}" was added successfully.'.format(
                address.line_1
            ))
            context.update({'success': True})
        else:
            context.update(add_address_form.errors)
        return JsonResponse(context)

