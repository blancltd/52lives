# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError

from . import choices as persons_choices
from .models import Person, Nominee


class NominateForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Person
        exclude = ('message', 'mobile_phone', 'title', 'created_at', 'updated_at', 'life',)

    def __init__(self, *args, **kwargs):
        super(NominateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['reason'].widget = forms.widgets.HiddenInput()
        self.fields['reason'].initial = persons_choices.REASON_TYPE_WOULD_LIKE_TO_NOMINATE


class NomineeForm(forms.ModelForm):
    required_css_class = 'required'
    confirm_email = forms.EmailField(label="Re-enter email address:")

    class Meta:
        model = Nominee
        fields = (
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'phone',
            'relation',
            'why_help',
            'what_need'
        )

    def __init__(self, *args, **kwargs):
        super(NomineeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['confirm_email'].required = True
        self.fields['phone'].required = True
        self.fields['relation'].required = True
        self.fields['why_help'].required = True
        self.fields['what_need'].required = True

    def clean(self):
        cleaned_data = super(NomineeForm, self).clean()

        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('confirm_email')

        if email != email_confirm:
            raise ValidationError({'confirm_email': ['The email addresses you entered do not match']})


NominatorFormSet = inlineformset_factory(
    Person,
    Nominee,
    form=NomineeForm,
    extra=0,
    min_num=1,
    can_delete=False
)


class SupportForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('created_at', 'updated_at', 'life',)

    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        self.fields['reason'].widget = forms.widgets.HiddenInput()
        self.fields['reason'].initial = persons_choices.REASON_TYPE_I_CAN_HELP
