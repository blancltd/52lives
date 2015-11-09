# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from countries.models import Country

from . import choices as addresses_choices
from . import help_text
from .managers import AddressManager


@python_2_unicode_compatible
class Address(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')
    type = models.IntegerField(
        choices=addresses_choices.ADDRESS_TYPES,
        default=addresses_choices.ADDRESS_TYPE_PRIMARY
    )
    description = models.CharField(
        max_length=20,
        null=True,
        help_text=help_text.ADDRESS['description']
    )
    company_name = models.CharField(max_length=200, null=True, blank=True)
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, null=True, blank=True)
    line_3 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=30)
    country = models.ForeignKey(Country, blank=True, null=True)
    default = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressManager()

    def __str__(self):
        return self.get_type_display()

    class Meta:
        verbose_name_plural = 'Addresses'
        ordering = ('-created_at',)

