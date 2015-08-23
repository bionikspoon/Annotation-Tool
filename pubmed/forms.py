#!/usr/bin/env python
# coding=utf-8

from django.forms import ModelForm
from .models import Entry

from braces.forms import UserKwargModelFormMixin


class EntryModelForm(UserKwargModelFormMixin, ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
