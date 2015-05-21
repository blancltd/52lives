# -*- coding: utf-8 -*-

from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
        )

