# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import CompanyListView, CompanyDetailView, CompanyLifeDetailView


urlpatterns = [
    url(
        r'^$',
        CompanyListView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        CompanyDetailView.as_view(),
        name='detail'
    ),
    url(
        r'^(?P<slug>[\w-]+)/(?P<life_number>\d+)/$',
        CompanyLifeDetailView.as_view(),
        name='life-detail'
    ),
]
