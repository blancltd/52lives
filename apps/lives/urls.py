# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import LivesListView, LiveDetailView


urlpatterns = [
    url(
        r'^$',
        LivesListView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        LiveDetailView.as_view(),
        name='detail'
    ),
]

