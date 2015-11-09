# -*- coding: utf-8 -*-

from django import template

from addresses.forms import AddressForm
from people.forms import NominatorFormSet

register = template.Library()


@register.assignment_tag
def get_nominee_form_set():
    return NominatorFormSet()


@register.assignment_tag
def get_address_form():
    return AddressForm()
