# -*- coding: utf-8 -*-

from blanc_pages_form_block.models import BaseFormBlock


class ContactFormBlock(BaseFormBlock):
    form_class = 'contacts.forms.ContactForm'


class SchoolContactFormBlock(BaseFormBlock):
    form_class = 'contacts.forms.SchoolContactForm'
