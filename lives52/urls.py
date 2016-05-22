# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from blanc_pages import block_admin


urlpatterns = [
    url(r'^news/', include('blanc_basic_news.urls', namespace='blanc_basic_news')),
    url(r'^lives/', include('lives.urls', namespace='lives')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blockadmin/', include(block_admin.site.urls)),
    url(r'^nominate/', include('people.urls', namespace='nominate')),
    url(r'^12lives/', include('companies.urls', namespace='companies')),
]


# Make it easier to see a 404 page under debug
if settings.DEBUG:
    from django.views.defaults import page_not_found

    urlpatterns += [
        url(r'^404/$', page_not_found),
    ]

# Serving static/media under debug
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
