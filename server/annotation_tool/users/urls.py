from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import UserListView, UserRedirectView, UserDetailView, UserUpdateView

urlpatterns = [

    # URL pattern for the UserListView
    url(  # :off
        regex=r'^$',
        view=UserListView.as_view(),
        name='list'
    ),  # :on

    # URL pattern for the UserRedirectView
    url(  # :off
        regex=r'^~redirect/$',
        view=UserRedirectView.as_view(),
        name='redirect'
    ),  # :on

    # URL pattern for the UserDetailView
    url(  # :off
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=UserDetailView.as_view(),
        name='detail'
    ),  # :on

    # URL pattern for the UserUpdateView
    url(  # :off
        regex=r'^~update/$',
        view=UserUpdateView.as_view(),
        name='update'
    ),  # :on

]
