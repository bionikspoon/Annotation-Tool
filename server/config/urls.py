from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

import config.api

urlpatterns = [  # :off

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include("annotation_tool.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^api/', include(config.api)),
    url(r'^(?P<path>(?:assets|scripts|styles)/.*)$','django.contrib.staticfiles.views.serve'),
    url('^$', TemplateView.as_view(template_name='index.html'))

]  # :on

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [url(r'^400/$', default_views.bad_request), url(r'^403/$', default_views.permission_denied),
                    url(r'^404/$', default_views.page_not_found), url(r'^500/$', default_views.server_error), ]
