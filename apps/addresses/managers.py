# -*- coding: utf-8 -*-

from django.db import models


class AddressManager(models.Manager):
    def create_address(self, address, obj, user):
        address.content_object = obj
        if user.is_authenticated():
            address.created_by = user
        address.save()
        return address
