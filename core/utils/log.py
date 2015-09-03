#!/usr/bin/env python
# coding=utf-8
import logging


class NotDjangoFilter(logging.Filter):
    def filter(self, record):
        return not record.name.startswith('django')
