# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe


PERSON_HELP_TEXTS = {
    'is_agreed': mark_safe(
        'Please ensure you have the permission of those involved before sharing personal details, '
        'and familiarise yourself with our <a href="/terms/">Terms and conditions</a> and '
        '<a href="/privacy/">data protection policy</a>.'
    )
}
