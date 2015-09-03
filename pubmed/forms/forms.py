#!/usr/bin/env python
# coding=utf-8
import logging

from django import forms
from django.forms import ModelForm
from crispy_forms import bootstrap, helper
from braces import forms as braces_forms
from model_utils import Choices

from ..models import EntryMeta
from .layouts import EntryFormLayout
from .fields import entryform_formfield_callback, TypedChoiceField

logger = logging.getLogger(__name__)


class EntryModelForm(braces_forms.UserKwargModelFormMixin, ModelForm):
    formfield_callback = entryform_formfield_callback

    treatment = TypedChoiceField(choices=Choices(*range(1, 6)), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = helper.FormHelper(self)
        self.helper.form_id = 'entry-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        self.helper.html5_required = True
        self.helper.layout = EntryFormLayout(helper=self.helper)

        self.helper.filter_by_widget(forms.RadioSelect).wrap(
            bootstrap.InlineRadios)

    def clean(self):
        cleaned_data = super().clean()
        treatment = int(cleaned_data.get('treatment') or 1)
        for i in range(treatment + 1, 6):
            cleaned_data['treatment_%s' % i] = ''

        return cleaned_data

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = EntryMeta.model
        fields = EntryMeta.public_fields
