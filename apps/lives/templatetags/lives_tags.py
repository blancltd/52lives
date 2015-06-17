# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from lives.models import Live


@register.assignment_tag
def get_latest_lives(number):
    return Live.objects.active()[:number]

