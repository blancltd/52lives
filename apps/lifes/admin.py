# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.utils import unquote
from django.contrib.contenttypes.admin import GenericTabularInline
from django.http import JsonResponse

from sorl.thumbnail.admin import AdminImageMixin

from notes.forms import NoteForm
from notes.models import Note

from .models import Life


class NoteInline(GenericTabularInline):
    template = 'admin/lifes/life/edit_inlines/tabular.html'
    model = Note
    extra = 1
    can_delete = False
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
        NoteInline,
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
            )
        ]
        return life_urls + urls

    def save_formset(self, request, form, formset, change):
        # TODO: Remove after is all done.
        notes = formset.save(commit=False)
        for note in notes:
            note.created_by = request.user
            note.save()

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, unquote(object_id))
        add_note_form = NoteForm()
        context = {
            'notes': obj.notes.all(),
            'add_note_form': add_note_form,
        }
        if extra_context:
            context.update(extra_context)
        return super(LifeAdmin, self).change_view(
            request, object_id, form_url, extra_context=context
        )

    def add_note(self, request, object_id):
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

