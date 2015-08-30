#!/usr/bin/env python
# coding=utf-8


class classproperty(object):
    def __init__(self, attr):
        self.attr = attr

    def __get__(self, _, owner):
        return self.attr(owner)
