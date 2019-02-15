# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField

from . import choices as persons_choices
from .models import Person, Nominee
from .help_texts import PERSON_HELP_TEXTS


class NominateForm(forms.ModelForm):
    required_css_class = 'required'
    confirm_email = forms.EmailField(label='Re-enter email address:')
    captcha = ReCaptchaField(label='Please tick this box to help us protect against spam messages')

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'home_phone',
            'hear_about_us',
            'captcha',
            'is_agreed',
            'reason',
        )


    def __init__(self, *args, **kwargs):
        super(NominateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['confirm_email'].required = True
        self.fields['reason'].widget = forms.widgets.HiddenInput()
        self.fields['reason'].initial = persons_choices.REASON_TYPE_WOULD_LIKE_TO_NOMINATE
        self.fields['is_agreed'].required = True
        self.fields['is_agreed'].help_text = PERSON_HELP_TEXTS['is_agreed_nominator']

    
    def clean(self):
        cleaned_data = super(NominateForm, self).clean()

        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError({'confirm_email': ['The email addresses you entered do not match']})


class NomineeForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Nominee
        exclude = ('person',)

    def __init__(self, *args, **kwargs):
        super(NomineeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['country'].required = True
        self.fields['relation'].required = True
        self.fields['why_help'].required = True
        self.fields['what_need'].required = True


NominatorFormSet = inlineformset_factory(
    Person,
    Nominee,
    form=NomineeForm,
    extra=0,
    min_num=1,
    can_delete=False
)


class SupportForm(forms.ModelForm):
    confirm_email = forms.EmailField(label='Re-enter email address:', required=False)
    captcha = ReCaptchaField(label='Please tick this box to help us protect against spam messages')

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'home_phone',
            'message',
            'hear_about_us',
            'captcha',
            'is_agreed',
            'reason'
        )

    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True
        self.fields['is_agreed'].widget.attrs['class'] = 'is-agreed_spaced'
        self.fields['reason'].widget = forms.widgets.HiddenInput()
        self.fields['reason'].initial = persons_choices.REASON_TYPE_I_CAN_HELP
    
    def clean(self):
        cleaned_data = super(SupportForm, self).clean()

        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        # Email isn't required here, so we only require confirmation if either
        # of the e-mail fields is not empty
        if (email or email_confirm) and email != email_confirm:
            raise ValidationError({'confirm_email': ['The email addresses you entered do not match']})
