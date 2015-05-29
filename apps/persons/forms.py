# -*- coding: utf-8 -*-

from django import forms

from . import choices as persons_choices
from .models import Person


class NominateForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('created_at', 'updated_at', 'life',)

    def __init__(self, *args, **kwargs):
        super(NominateForm, self).__init__(*args, **kwargs)
        self.fields['reason'].widget = forms.widgets.HiddenInput()
        self.fields['reason'].initial = persons_choices.REASON_TYPE_WOULD_LIKE_TO_NOMINATE
