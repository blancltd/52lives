# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import LivesListView


urlpatterns = [
    url(
        r'^$',
        LivesListView.as_view(),
        name='list'
    ),
]

