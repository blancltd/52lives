# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import CompanyListView


urlpatterns = [
    url(
        r'^$',
        CompanyListView.as_view(),
        name='list'
    ),
    # url(
    #     r'^(?P<slug>[\w-]+)/$',
    #     CompanyLifeListView.as_view(),
    #     name='list'
    # ),
]
