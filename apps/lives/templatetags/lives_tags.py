# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from lives.models import Life


@register.assignment_tag
def get_latest_lives(number):
    return Life.objects.active()[:number]


@register.assignment_tag
def get_latest_life(default):
    if default:
        return default

    try:
        return Life.objects.active().latest()
    except Life.DoesNotExist:
        return None
