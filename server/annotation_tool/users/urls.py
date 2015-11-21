# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    
    # URL pattern for the UserListView
    url(  # :off
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),  # :on

    # URL pattern for the UserRedirectView
    url(  # :off
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),  # :on

    # URL pattern for the UserDetailView
    url(  # :off
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),  # :on

    # URL pattern for the UserUpdateView
    url(  # :off
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),  # :on

]
