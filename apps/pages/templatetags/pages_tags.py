# -*- coding: utf-8 -*-

from blanc_pages import get_page_model

from django import template

from mptt.templatetags.mptt_tags import cache_tree_children


register = template.Library()


@register.assignment_tag
def footer_pages():
    page_qs = get_page_model().objects.exclude(level__gt=1)
    return cache_tree_children(page_qs)


@register.filter
def show_nav(pages):
    return [x for x in pages if x.show_in_navigation]

