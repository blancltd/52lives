# -*- coding: utf-8 -*-

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from countries.models import Country
from lives import choices as live_choices
from lives.models import Life

from . import choices as persons_choices
from .help_texts import PERSON_HELP_TEXTS
from .managers import NominatorManager


@python_2_unicode_compatible
class Person(models.Model):
    life = models.ForeignKey(Life, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    home_phone = models.CharField('Phone', max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    reason = models.IntegerField(choices=persons_choices.REASON_TYPES)
    message = models.TextField(blank=True)
    hear_about_us = models.CharField('How did you hear about us?', max_length=120)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_agreed = models.BooleanField(default=False, help_text=PERSON_HELP_TEXTS['is_agreed'])

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)


class Nominator(Person):
    objects = NominatorManager()

    class Meta:
        proxy = True


class Nominee(models.Model):
    person = models.ForeignKey(Person)
    first_name = models.CharField(max_length=20, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    relation = models.CharField('How do you know the nominee?', max_length=124, blank=True)
    why_help = models.TextField('Why do they need help?', blank=True)
    what_need = models.TextField('What do they need?', blank=True)

    class Meta:
        verbose_name_plural = 'Nominee'
