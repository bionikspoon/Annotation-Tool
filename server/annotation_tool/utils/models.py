#!/usr/bin/env python
# coding=utf-8

from model_utils import Choices

__all__ = ['choices']


def _upper_or_int(arg):
    try:
        return arg.upper()
    except AttributeError:
        return arg


def choices(*args):
    return Choices(*((_upper_or_int(arg), arg) for arg in args))
