# -*- coding: utf-8 -*-

from django.db import models

from . import choices as people_choices


class NominatorManager(models.Manager):
    def get_queryset(self):
        return super(NominatorManager, self).get_queryset().filter(
            reason=people_choices.REASON_TYPE_WOULD_LIKE_TO_NOMINATE
        )
