# -*- coding: utf-8 -*-

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at',)
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'subject': 'Your subject',
            'content': 'Your content',
        }
