#!/usr/bin/env python
# coding=utf-8
from django import forms
from django.forms import ModelForm
from django.db import models
from crispy_forms import layout, bootstrap, helper as crispy_helper
from braces.forms import UserKwargModelFormMixin
from model_utils import Choices

from .models import EntryMeta

models.BLANK_CHOICE_DASH[0] = ('', 'Null')


class SubmitContext(layout.Submit):
    def render(self, form, form_style, context, **kwargs):
        self.value = context.get('action_text') or self.value
        return super().render(form, form_style, context, **kwargs)


class ModelChoiceField(forms.ModelChoiceField):
    widget = forms.RadioSelect

    def __init__(self, empty_label=models.BLANK_CHOICE_DASH[0][1], *args,
                 **kwargs):
        super().__init__(empty_label=empty_label, *args, **kwargs)


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

    treatment = TypedChoiceField(choices=Choices(*range(1, 6)))

    @property
    def helper(self):
        helper = crispy_helper.FormHelper(self)
        helper.form_id = 'entry-form'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-xs-4 col-md-3 col-lg-2'
        helper.field_class = 'col-xs-8 col-md-9 col-lg-10'
        helper.html5_required = True
        helper.layout = layout.Layout(

            layout.Fieldset(

                'Pubmed',

                'pubmed_id', ),

            layout.Fieldset('Gene Description',

                            'gene', 'structure', 'mutation_type', 'syntax',
                            'syntax_text', 'operator', 'rule_level',

                            layout.Row(

                                layout.Column(

                                    'chromosome', 'start', 'stop',
                                    'breakend_strand', 'breakend_direction',

                                    css_class='col-sm-6',
                                    data_form_column='true'

                                ),

                                layout.HTML('<hr class="visible-xs">'),

                                layout.Column(

                                    'mate_chromosome', 'mate_start', 'mate_end',
                                    'mate_breakend_strand',
                                    'mate_breakend_direction',

                                    css_class='col-sm-6',
                                    data_form_column='true'

                                ),

                                css_class='well',

                            ),

                            'minimum_number_of_copies',
                            'maximum_number_of_copies', 'coordinate_predicate',
                            'partner_coordinate_predicate', 'variant_type',
                            'variant_consequence', 'variant_clinical_grade',

                            ),

            layout.Fieldset('Treatment',

                            'disease',

                            'treatment',

                            'treatment_1', 'treatment_2', 'treatment_3',
                            'treatment_4', 'treatment_5'

                            ),

            layout.Fieldset('Study',

                            'population_size', 'sex', 'ethnicity',
                            'assessed_patient_outcomes',
                            'significant_patient_outcomes', 'design',
                            'reference_claims', 'comments'

                            ),

            layout.Fieldset('{{ action_text }} Entry',

                            bootstrap.FormActions(

                                layout.Submit('submit', 'Submit'),
                                layout.Button('cancel', 'Cancel')

                            ),

                            ),

        )

        helper.filter_by_widget(forms.RadioSelect).wrap(bootstrap.InlineRadios)
        return helper

    def clean(self):
        cleaned_data = super().clean()
        treatment = int(cleaned_data.get('treatment'))
        for i in range(treatment + 1, 6):
            cleaned_data['treatment_%s' % i] = ''

        return cleaned_data

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = EntryMeta.model
        fields = EntryMeta.public_fields
