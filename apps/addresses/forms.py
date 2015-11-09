# -*- coding: utf-8 -*-

from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Address
        fields = (
            'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
        )

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = True
