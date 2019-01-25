# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact, SchoolContact


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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True


class SchoolContactForm(forms.ModelForm):
    class Meta:
        model = SchoolContact
        exclude = ('created_at',)
        labels = {
            'name': 'Your name',
            'position': 'Your position',
            'telephone': 'Your telephone',
            'email': 'Your email',
            'workshop_date': 'Preferred workshop date',
            'hear_about': 'How did you hear about us?',
        }

    def clean(self):
        cleaned_data = super(SchoolContactForm, self).clean()
        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError('The email addresses you entered do not match')
