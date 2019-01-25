# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe


CONTACT_HELP_TEXTS = {
    'is_agreed': mark_safe(
        'Before submitting this form, please '
        '<a href="/privacy/">'
        'click here to read our privacy policy'
        '</a> '
        'and tick this box to confirm that you have read the policy notice and consent to the '
        'processing of your personal data and sensitive personal data.'
    )
}
