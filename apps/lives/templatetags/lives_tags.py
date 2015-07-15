# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from lives.models import Life


@register.assignment_tag
def get_latest_lives(number):
    return Life.objects.active()[:number]

