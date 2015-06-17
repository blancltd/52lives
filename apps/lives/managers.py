# -*- coding: utf-8 -*-

from django.db import models


class LiveManager(models.Manager):

    def active(self):
        """ Return lives with number. """
        qs = self.get_queryset()
        qs = qs.filter(number__isnull=False)
        return qs

    def unactive(self):
        """ Return lives without number. """
        qs = self.get_queryset()
        qs = qs.filter(number__isnull=True)
        return qs

