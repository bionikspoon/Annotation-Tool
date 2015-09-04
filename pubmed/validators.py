#!/usr/bin/env python
# coding=utf-8
from django.core.exceptions import ValidationError


def validate_pubmed_id(value):
    if not str(value).endswith('000'):
        msg = "Must end with '000'."
        raise ValidationError(msg)
