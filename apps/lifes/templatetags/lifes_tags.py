# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from lifes.models import Life


@register.assignment_tag
def get_latest_lifes(number):
    return Life.objects.active()[:number]

