# -*- coding: utf-8 -*-

from django.db import models

from . import help_text


class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list.
    The field names are a bit awkward, but kept for backwards compatibility.
    pycountry's syntax of alpha2, alpha3, name and official_name seems sane.
    """
    name = models.CharField(
        'Country name',
        max_length=128,
        help_text=help_text.COUNTRY['name'],
    )
    iso_3166_1_a2 = models.CharField(
        'ISO 3166-1 alpha-2',
        max_length=2,
        blank=True,
        help_text=help_text.COUNTRY['iso_3166_1_a2']
    )

    iso_3166_1_a3 = models.CharField(
        'ISO 3166-1 alpha-3',
        max_length=3,
        blank=True,
        help_text=help_text.COUNTRY['iso_3166_1_a2'],
    )
    iso_3166_1_numeric = models.CharField(
        'ISO 3166-1 numeric',
        blank=True,
        max_length=3,
        help_text=help_text.COUNTRY['iso_3166_1_a2'],
    )

    display_order = models.PositiveSmallIntegerField(
        "Display order",
        default=0,
        db_index=True,
        help_text=help_text.COUNTRY['display_order']
    )

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

