# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation

from sorl.thumbnail import ImageField

from notes.models import Note

from . import help_text
from . import choices as life_choices


@python_2_unicode_compatible
class Life(models.Model):
    title = models.CharField(max_length=10, choices=life_choices.SOCIAL_TITLE_CHOICES)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    number = models.PositiveIntegerField(help_text.LIFE['number'], blank=True, null=True)
    image = ImageField(
        help_text.LIFE['image'],
        blank=True,
        upload_to='uploads/lifes/life/%Y/%m/%d'
    )
    content = models.TextField(help_text.LIFE['content'])
    request = models.TextField(help_text.LIFE['request'])
    summary = models.TextField(help_text.LIFE['summary'], blank=True)
    thank_you = models.TextField(help_text.LIFE['thank_you'], blank=True)
    is_published = models.BooleanField(help_text.LIFE['is_published'], default=False)
    notes = GenericRelation(Note)
    slug = models.SlugField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return u'{} {} {}'.format(self.title, self.first_name, self.last_name)
