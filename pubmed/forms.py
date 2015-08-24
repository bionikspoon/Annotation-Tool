#!/usr/bin/env python
# coding=utf-8

from django.forms import ModelForm

# noinspection PyPackageRequirements
from braces.forms import UserKwargModelFormMixin

from .models import Entry


class EntryModelForm(UserKwargModelFormMixin, ModelForm):
    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Entry
        fields = '__all__'
