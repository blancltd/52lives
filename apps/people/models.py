# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from lives import choices as live_choices
from lives.models import Life

from . import choices as persons_choices


@python_2_unicode_compatible
class Person(models.Model):
    life = models.ForeignKey(Life, blank=True, null=True)
    title = models.CharField(max_length=10, choices=live_choices.SOCIAL_TITLE_CHOICES)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    home_phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    reason = models.IntegerField(choices=persons_choices.REASON_TYPES)
    message = models.TextField()
    hear_about_us = models.CharField(max_length=120)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return u'{} {} {}'.format(self.title, self.first_name, self.last_name)

