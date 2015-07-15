# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .blocks.forms import ContactFormBlock  # noqa


@python_2_unicode_compatible
class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'{0} {1}'.format(self.name, self.email)

    def format_email(self):
        message = """From email: {} \nName: {} \nContent: \n{}'""".format(
            self.email, self.name, self.content
        )
        return message

