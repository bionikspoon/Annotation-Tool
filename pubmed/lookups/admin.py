#!/usr/bin/env python
# coding=utf-8
from django.contrib import admin

from .models import LookupTable

lookup_tables = (lookup_table for lookup_table in LookupTable.__subclasses__())


@admin.register(*lookup_tables)
class LookupTableAdmin(admin.ModelAdmin):
    fields = ('choice',)
    list_display = ('choice', 'id', 'created', 'modified')
