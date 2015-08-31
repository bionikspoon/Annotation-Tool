#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from annotation_tool.users.views import UserViewSet
from pubmed.views import EntryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pubmed', EntryViewSet)

urlpatterns = [

    url(r'^', include(router.urls))

]
