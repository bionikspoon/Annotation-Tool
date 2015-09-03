#!/usr/bin/env python
# coding=utf-8
import logging

from django.conf import settings


class NotDjangoFilter(logging.Filter):
    def filter(self, record):
        return not record.name.startswith('django')


class NotProductionFilter(logging.Filter):
    def filter(self, record):
        return settings.DJANGO_SETTINGS_MODULE != 'config.settings.production'
