#!/usr/bin/env python
# coding=utf-8
"""
Custom fields for pubmed.
"""

from django import forms
from django.db import models

models.BLANK_CHOICE_DASH[0] = ('', 'Null')


class ModelChoiceField(forms.ModelChoiceField):
    """
    Override blank choice text. (From '--------' to 'Null').

    :type empty_label: str
    :param args:
    :param kwargs:
    """
    widget = forms.RadioSelect

    def __init__(self, empty_label=models.BLANK_CHOICE_DASH[0][1], *args,
                 **kwargs):
        super().__init__(empty_label=empty_label, *args, **kwargs)


class TypedChoiceField(forms.TypedChoiceField):
    """
    User radio select widgets for `TypedChoiceField`s
    """
    widget = forms.RadioSelect


def entryform_formfield_callback(field, **kwargs):
    """
    Use radio inline widget by default.

    :type field: PositiveIntegerField or CharField or ForeignKey or
    ManyToManyField or TextField
    :param kwargs:
    :return:
    """
    if isinstance(field, models.ForeignKey):
        return field.formfield(form_class=ModelChoiceField, **kwargs)
    if isinstance(field, models.IntegerField):
        return field.formfield(choices_form_class=TypedChoiceField, **kwargs)
    else:
        return field.formfield(**kwargs)
