#!/usr/bin/env python
# coding=utf-8
from crispy_forms.bootstrap import InlineRadios, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Layout, Fieldset, Button, Row, Column,
    HTML, Field, MultiField, Div)
from django import forms
from django.db.models import BLANK_CHOICE_DASH
from django.forms import ModelForm
from django.db import models
from braces.forms import UserKwargModelFormMixin
from model_utils import Choices

from .models import Entry

BLANK_CHOICE_DASH[0] = ("", "Null")


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


class TypedChoiceField(forms.TypedChoiceField):
    widget = forms.RadioSelect


def formfield_callback(field, **kwargs):
    if isinstance(field, models.ForeignKey):
        return field.formfield(form_class=ModelChoiceField, **kwargs)
    if isinstance(field, models.IntegerField):
        return field.formfield(choices_form_class=TypedChoiceField, **kwargs)
    else:
        return field.formfield(**kwargs)


class EntryModelForm(UserKwargModelFormMixin, ModelForm):
    formfield_callback = formfield_callback

    treatment = forms.TypedChoiceField(choices=Choices(*range(1, 6)))

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.form_id = 'entry-form'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        helper.field_class = 'col-xs-8 col-md-9 col-lg-10'
        helper.html5_required = True
        helper.layout = Layout(

            Fieldset(

                'Pubmed',

                'pubmed_id', ),

            Fieldset('Gene Description',

                     'gene', 'structure', 'mutation_type', 'syntax',
                     'syntax_text', 'operator', 'rule_level',

                     Row(

                         Column(

                             Field('chromosome',wrapper_class=''), 'start', 'stop', 'breakend_strand',
                             'breakend_direction',

                             css_class='col-lg-6'

                         ),

                         HTML('<hr class="hidden-lg">'),

                         Column(

                             'mate_chromosome', 'mate_start', 'mate_end',
                             'mate_breakend_strand', 'mate_breakend_direction',

                             css_class='col-lg-6'

                         ),

                         css_class='well',

                     ),

                     'minimum_number_of_copies', 'maximum_number_of_copies',
                     'coordinate_predicate', 'partner_coordinate_predicate',
                     'variant_type', 'variant_consequence',
                     'variant_clinical_grade',

                     ),

            Fieldset('Treatment',

                     'disease',

                     Field('treatment',
                           data_minimum_results_for_search='Infinity'),

                     'treatment_1', 'treatment_2', 'treatment_3', 'treatment_4',
                     'treatment_5'

                     ),

            Fieldset('Study',

                     'population_size', 'sex', 'ethnicity',
                     'assessed_patient_outcomes',
                     'significant_patient_outcomes', 'design',
                     'reference_claims', 'comments'

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
