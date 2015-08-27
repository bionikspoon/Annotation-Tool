#!/usr/bin/env python
# coding=utf-8
from crispy_forms.bootstrap import InlineField, InlineRadios, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Field, Layout, Fieldset, Button,
                                 MultiField, Div)
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
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        helper.field_class = 'col-xs-8 col-md-9 col-lg-10'
        helper.html5_required = True
        helper.layout = Layout(

            Fieldset(

                'Pubmed', 'pubmed_id', ),

            Fieldset(

                'Gene Description', 'gene', 'structure', 'mutation_type',
                'syntax', 'syntax_text', 'operator', 'rule_level',

                Div(

                    'chromosome', 'start', 'stop', 'breakend_strand',
                    'breakend_direction',

                    css_class='well well-sm'

                ),

                Div(

                    'mate_chromosome', 'mate_start', 'mate_end',
                    'mate_breakend_strand',

                    css_class='well well-sm'

                ),

                'minimum_number_of_copies', 'maximum_number_of_copies',
                'coordinate_predicate', 'partner_coordinate_predicate',
                'variant_type', 'variant_consequence', 'variant_clinical_grade',

            ),

            Fieldset(

                'Treatment', 'disease', 'treatment_1', 'treatment_2',
                'treatment_3', 'treatment_4', 'treatment_5'

            ),

            Fieldset(

                'Study', 'population_size', 'sex', 'ethnicity',
                'assessed_patient_outcomes', 'significant_patient_outcomes',
                'design', 'reference_claims', 'comments'

            ),

            FormActions(

                Submit('save', '{{ action_text }} Entry'),
                Button('cancel', 'Cancel')

            )

        )

        helper.filter_by_widget(forms.RadioSelect).wrap(InlineRadios)
        return helper

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Entry
        fields = '__all__'
