#!/usr/bin/env python
# coding=utf-8

class GeneDatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model and model.__qualname__ is 'Gene':
            return 'genes'
        return None

    def db_for_write(self, model, **hints):
        if model and model.__qualname__ is 'Gene':
            return 'genes'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if 'Gene' in [obj1.__qualname__, obj2.__qualname__]:
            return False

        return None

    # noinspection PyUnusedLocal
    def allow_migrate(self, db, app_label, model=None, **hints):
        if db is 'genes':
            return model and model.__qualname__ is 'Gene'

        if model and model.__qualname__ is 'Gene':
            return False

        return None
