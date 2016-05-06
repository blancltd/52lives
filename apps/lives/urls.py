# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf.urls import url

from .views import LivesListView, LifeDetailView


urlpatterns = [
    url(
        r'^$',
        LivesListView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<slug>[0-9]+)/$',
        LifeDetailView.as_view(),
        name='detail'
    ),
]
