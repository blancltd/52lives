# -*- coding: utf-8 -*-

from blanc_pages_form_block.models import BaseFormBlock


class NominateFormBlock(BaseFormBlock):
    form_class = 'people.forms.NominateForm'
    render_function = 'blanc_pages_form_block.views.form_view'
