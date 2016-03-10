# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from sorl.thumbnail import ImageField

from lives import choices as life_choices
from lives import help_text


@python_2_unicode_compatible
class Company(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = ImageField(
        blank=True,
        upload_to='uploads/companies/company/%Y/%m/%d'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Life(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(
        max_length=10,
        choices=life_choices.SOCIAL_TITLE_CHOICES,
        blank=True,
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    number = models.PositiveIntegerField(
        help_text.LIVE['number'], blank=True, null=True, unique=True)
    image = ImageField(
        help_text.LIVE['image'],
        blank=True,
        upload_to='uploads/companies/life/%Y/%m/%d'
    )
    email = models.EmailField(blank=True)
    home_phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    request_title = models.CharField(max_length=100)
    content = models.TextField(help_text.LIVE['content'])
    request = models.TextField(help_text.LIVE['request'])
    summary = models.TextField(help_text.LIVE['summary'], blank=True)
    thank_you = models.TextField(help_text.LIVE['thank_you'], blank=True)
    is_published = models.BooleanField(help_text.LIVE['is_published'], default=False)
    slug = models.SlugField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    def get_full_name(self):
        return u'{} {} {}'.format(self.title, self.first_name, self.last_name)
    get_full_name.short_description = 'Full name'
