# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^form/$', views.NomineeCreateView.as_view(), name='form')
]
