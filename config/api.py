#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url, include

from pubmed.urls import api_urlpatterns as pubmed

urlpatterns = [

    url(r'^pubmed/', include(pubmed))

]