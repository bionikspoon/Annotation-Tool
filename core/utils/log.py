#!/usr/bin/env python
# coding=utf-8
"""
Utilities for log config.
"""
import logging

from django.conf import settings


class NotDjangoFilter(logging.Filter):
    """
    Filter out 'django' loggers.
    """

    def filter(self, record) -> bool:
        """
        Check if starts with 'django'.

        :param record:
        :return: False if begins with 'django'.
        """
        return not record.name.startswith('django')


class NotProductionFilter(logging.Filter):
    """
    Filter by config settings.
    """

    def filter(self, record) -> bool:
        """
        Check if running in production config.

        :param record:
        :return: False if 'config.settings.production'.
        """
        return settings.DJANGO_SETTINGS_MODULE != 'config.settings.production'
