#!/usr/bin/env python
# coding=utf-8

from whitenoise.django import HelpfulExceptionMixin
from whitenoise.storage_backport import ManifestStaticFilesStorage


class GeneDatabaseRouter(object):
    def db_for_read(self, model, **hints):
        # print('read::%r' % model._meta.app_label)
        if model._meta.app_label == 'gene':
            # print('read::%r' % model._meta.app_label)
            return 'genes'
        return None

    def db_for_write(self, model, **hints):
        # print('write::%r' % model._meta.app_label)

        if model._meta.app_label == 'gene':
            # print('write::%r' % model._meta.app_label)
            return 'genes'

        return None

    def allow_relation(self, obj1, obj2, **hints):

        # print('%s <> %s' % (obj1._meta.app_label, obj2._meta.app_label))
        if obj1._meta.app_label == 'gene' and obj2._meta.app_label == 'gene':
            return True

        return None
        #

    # noinspection PyUnusedLocal
    def allow_migrate(self, db, app_label, model=None, **hints):
        # print('migrate::%r:%r' % (db, app_label))
        if app_label == 'gene':
            return bool(db == 'genes')

        if db == 'genes':
            return False

        return None


class AnnotationToolStaticFilesStorage(HelpfulExceptionMixin, ManifestStaticFilesStorage):
    pass
