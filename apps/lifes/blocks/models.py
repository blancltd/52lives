# -*- coding: utf-8 -*-

from django.db import models

from blanc_pages.blocks import BaseBlock

from lifes.models import Life


class LatestLifesBlock(BaseBlock):
    number_of_lives = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = 'Latest lifes'


class LifeBlock(BaseBlock):
    life = models.ForeignKey(
        Life,
        blank=True,
        null=True,
        limit_choices_to={'number__isnull': False}
    )

    class Meta:
        verbose_name = 'Life'

