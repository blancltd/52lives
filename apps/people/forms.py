# -*- coding: utf-8 -*-

from django import forms

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

    class Meta:
        model = Nominee
        exclude = ('person',)

    def __init__(self, *args, **kwargs):
        super(NomineeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone'].required = True
        self.fields['email'].required = True
        self.fields['relation'].required = True
        self.fields['why_help'].required = True
        self.fields['what_need'].required = True


from django.forms import inlineformset_factory
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
