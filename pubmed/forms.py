#!/usr/bin/env python
# coding=utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.forms import ModelForm

# noinspection PyPackageRequirements
from braces.forms import UserKwargModelFormMixin

from .models import Entry


class EntryModelForm(UserKwargModelFormMixin, ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        self.helper.field_class = 'col-xs-8 col-md-9 col-lg-10'

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Entry
        fields = '__all__'

