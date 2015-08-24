#!/usr/bin/env python
# coding=utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(SubmitContext('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        self.helper.field_class = 'col-xs-8 col-md-9 col-lg-10'

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Entry
        fields = '__all__'
