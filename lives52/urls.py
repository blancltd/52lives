from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lives52.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
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
