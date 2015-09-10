"""
Project URL configuration.
"""

# Compatibility
from __future__ import unicode_literals

# Django Packages
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

# Annotation Tool Project
import config

urlpatterns = [

    url(r'^$', RedirectView.as_view(pattern_name='pubmed:list', permanent=False), name="home"),

    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/', include(config.api)),

    # Django Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/ui/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("annotation_tool.users.urls", namespace="users")),

    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^pubmed/', include('pubmed.urls', namespace='pubmed')),

    url(r'^google51945c962ca81cb4.html$',
        TemplateView.as_view(template_name='google/google51945c962ca81cb4.html'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # Debug error pages
    urlpatterns += [

        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),

    ]
