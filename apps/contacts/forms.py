# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField

from .models import Contact, SchoolContact


class ContactForm(forms.ModelForm):
    confirm_email = forms.EmailField()
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'confirm_email',
            'subject',
            'content',
            'captcha',
            'is_agreed',
        )
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'subject': 'Your subject',
            'content': 'Your content',
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['confirm_email'].label = 'Re-enter your email'
        self.fields['captcha'].label = 'Please tick this box to help us protect against spam messages'
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
            'workshop_date': """Please enter 3 preferred dates for your workshop (we will do our
                                best to accommodate one of the dates)""",
            'hear_about': 'How did you hear about us?',
        }

    def __init__(self, *args, **kwargs):
        super(SchoolContactForm, self).__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True
        self.fields['is_agreed'].widget.attrs['class'] = 'is-agreed_spaced'
        self.fields['workshop_date'].widget.attrs['rows'] = 3
        self.fields['workshop_date'].widget.attrs['style'] = 'resize: none'

    def clean(self):
        cleaned_data = super(SchoolContactForm, self).clean()
        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError('The email addresses you entered do not match')
