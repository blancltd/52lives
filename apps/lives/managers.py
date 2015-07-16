# -*- coding: utf-8 -*-

from django.db import models


class LifeManager(models.Manager):

    def active(self):
        """ Return lives with number. """
        qs = self.get_queryset()
        qs = qs.filter(is_published=True)
        return qs

    def unactive(self):
        """ Return lives without number. """
        qs = self.get_queryset()
        qs = qs.filter(is_published=False)
        return qs
