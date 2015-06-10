# -*- coding: utf-8 -*-

from django.db import models

from blanc_pages.blocks import BaseBlock


class LatestLivesBlock(BaseBlock):
    number_of_lives = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = 'Latest lives'

