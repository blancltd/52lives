# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from sorl.thumbnail import ImageField

from notes.models import Note

from . import help_text
from . import choices as life_choices
from .blocks.models import LatestLivesBlock, LiveBlock  # noqa
from .managers import LifeManager


@python_2_unicode_compatible
class Life(models.Model):
    nominee = models.CharField(max_length=120)
    title = models.CharField(
        max_length=10,
        choices=life_choices.SOCIAL_TITLE_CHOICES,
        blank=True,
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    number = models.PositiveIntegerField(
        help_text.LIVE['number'], blank=True, null=True, unique=True
    )
    image = ImageField(
        help_text.LIVE['image'],
        blank=True,
        upload_to='uploads/lives/live/%Y/%m/%d'
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
    notes = GenericRelation(Note)
    slug = models.SlugField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = LifeManager()

    class Meta:
        get_latest_by = 'id'
        ordering = ('-number',)
        verbose_name_plural = 'Lives'

    def __str__(self):
        return u'{}'.format(self.nominee)

    def get_absolute_url(self):
        return reverse('lives:detail', args=[str(self.number)])

    def clean(self):
        if self.is_published and not self.number:
            raise ValidationError('Published lives need a life number')

        if self.is_published and not self.image:
            raise ValidationError('Published lives need an image')

    def get_full_name(self):
        return u'{} {} {}'.format(self.title, self.first_name, self.last_name)
    get_full_name.short_description = 'Full name'
