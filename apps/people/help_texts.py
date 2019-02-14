# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe


PERSON_HELP_TEXTS = {
    'is_agreed_nominator': mark_safe(
        """Before submitting your nomination, please 
           <a href="https://52lives.contentfiles.net/media/assets/file/Final_Privacy_Notice_Nominator_Q0KzKUJ.pdf">click here to read our privacy notice</a> 
           and tick this box to confirm that you have read the policy notice and consent to the 
           processing of your personal data and sensitive personal data."""
    ),
    'is_agreed': mark_safe(
        """Before submitting this form, please
           <a href="/privacy/">click here to read our privacy policy</a>
           and tick this box to confirm that you have read the policy notice and consent to the 
           processing of your personal data and sensitive personal data."""
    )
}
