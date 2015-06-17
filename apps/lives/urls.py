# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import LivesListView, LifeDetailView


urlpatterns = [
    url(
        r'^$',
        LivesListView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        LifeDetailView.as_view(),
        name='detail'
    ),
]

