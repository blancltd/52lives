# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact, SchoolContact


class ContactForm(forms.ModelForm):
    confirm_email = forms.EmailField()

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'confirm_email',
            'subject',
            'content',
            'is_agreed',
        )
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'confirm_email': 'Re-enter your email:',
            'subject': 'Your subject',
            'content': 'Your content',
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True
        self.fields['is_agreed'].widget.attrs['class'] = 'is-agreed_spaced'

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()

        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError({'confirm_email': ['The email addresses you entered do not match']})


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

    def __init__(self, *args, **kwargs):
        super(SchoolContactForm, self).__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True
        self.fields['is_agreed'].widget.attrs['class'] = 'is-agreed_spaced'

    def clean(self):
        cleaned_data = super(SchoolContactForm, self).clean()
        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError('The email addresses you entered do not match')
