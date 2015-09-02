#!/usr/bin/env python
# coding=utf-8

from django import forms
from django.db import models

models.BLANK_CHOICE_DASH[0] = ('', 'Null')


class ModelChoiceField(forms.ModelChoiceField):
    widget = forms.RadioSelect

    def __init__(self, empty_label=models.BLANK_CHOICE_DASH[0][1], *args,
                 **kwargs):
        super().__init__(empty_label=empty_label, *args, **kwargs)


class TypedChoiceField(forms.TypedChoiceField):
    widget = forms.RadioSelect


def entryform_formfield_callback(field, **kwargs):
    if isinstance(field, models.ForeignKey):
        return field.formfield(form_class=ModelChoiceField, **kwargs)
    if isinstance(field, models.IntegerField):
        return field.formfield(choices_form_class=TypedChoiceField, **kwargs)
    else:
        return field.formfield(**kwargs)
