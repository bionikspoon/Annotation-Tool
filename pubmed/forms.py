#!/usr/bin/env python
# coding=utf-8
from crispy_forms.bootstrap import InlineField, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout
from django import forms

from django.forms import ModelForm
from django.db import models

from braces.forms import UserKwargModelFormMixin

from .models import Entry


class SubmitContext(Submit):
    def render(self, form, form_style, context, **kwargs):
        self.value = context.get('action_text') or self.value
        return super().render(form, form_style, context, **kwargs)


class ModelChoiceField(forms.ModelChoiceField):
    widget = forms.RadioSelect
    empty_label = 'Null'

    def __init__(self, empty_label='Null', widget=forms.RadioSelect, *args,
                 **kwargs):
        super().__init__(empty_label=empty_label, widget=widget, *args,
                         **kwargs)


def formfield_callback(field, **kwargs):
    if isinstance(field, models.ForeignKey):
        return field.formfield(form_class=ModelChoiceField, **kwargs)
    else:
        return field.formfield(**kwargs)


class EntryModelForm(UserKwargModelFormMixin, ModelForm):
    formfield_callback = formfield_callback

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.add_input(SubmitContext('submit', 'Submit'))
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        helper.field_class = 'col-xs-8 col-md-9 col-lg-10'
        helper.html5_required = True
        helper.filter_by_widget(forms.RadioSelect).wrap(InlineRadios)
        return helper

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Entry
        fields = '__all__'
