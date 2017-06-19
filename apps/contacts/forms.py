# -*- coding: utf-8 -*-

from django import forms

from .models import Contact, ContactUs


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


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('created_at',)
        labels = {
            'name': 'Your name',
            'position': 'Your position',
            'telephone': 'Your telephone',
            'email': 'Your email',
            'workshop_date': 'Preferred workshop date',
            'hear_about': 'How did you hear about us?',
        }
