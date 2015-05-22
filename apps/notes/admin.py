# -*- coding: utf-8 -*-

from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import messages

from .forms import NoteForm
from .models import Note


class NoteInline(GenericTabularInline):
    template = 'admin/notes/note/edit_inlines/notes.html'
    dialog_data = {
        'form': NoteForm(),
        'title': 'Add note',
        'dialog_class': 'add-note-dialog',
        'form_class': 'add-note-form',
    }
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

    class Media:
        js = ('js/admin/notes/notes.js',)

    @staticmethod
    def create_note(request, obj):
        """ Add note. """
        context = {}
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.content_object = obj
            note.created_by = request.user
            note.save()
            messages.success(request, 'The note "{}" was added successfully.'.format(
                note.note
            ))
            context.update({'success': True})
        else:
            context.update(note_form.errors)
        return context

