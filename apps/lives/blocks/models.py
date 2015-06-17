# -*- coding: utf-8 -*-

from django.db import models

from blanc_pages.blocks import BaseBlock

from lives.models import Live


class LatestLivesBlock(BaseBlock):
    number_of_lives = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = 'Latest lives'


class LiveBlock(BaseBlock):
    live = models.ForeignKey(
        Live,
        blank=True,
        null=True,
        limit_choices_to={'number__isnull': False}
    )

    class Meta:
        verbose_name = 'Live'

