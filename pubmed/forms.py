#!/usr/bin/env python
# coding=utf-8
import logging

from crispy_forms.utils import flatatt, render_field
from django import forms
from django.forms import ModelForm
from django.db import models
from crispy_forms import layout, bootstrap, helper
from braces import forms as braces_forms
from django.template.loader import render_to_string
from model_utils import Choices

from .models import EntryMeta

logger = logging.getLogger(__name__)
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


class Flat(layout.LayoutObject):
    template = "flat/layout/flat.html"

    def __init__(self, *fields, **kwargs):
        self.fields = list(fields)
        self.css_class = kwargs.pop('css_class', '')
        self.css_id = kwargs.pop('css_id', None)
        self.template = kwargs.pop('template', self.template)
        self.flat_attrs = flatatt(kwargs)

    def get_rendered_fields(self, form, form_style, context,
                            template_pack='flat', **kwargs):
        kwargs['template'] = 'flat/layout/field.html'

        return ''.join(
            render_field(field, form, form_style, context, template_pack='flat',
                         **kwargs) for field in self.fields)

    def render(self, form, form_style, context, template_pack='flat', **kwargs):
        fields = self.get_rendered_fields(form, form_style, context,
                                          template_pack, **kwargs)

        template = self.get_template_name(template_pack)
        return render_to_string(template, {
            'fieldset': self,
            'fields': fields,
            'form_style': form_style
        })


class EntryModelForm(braces_forms.UserKwargModelFormMixin, ModelForm):
    formfield_callback = formfield_callback

    treatment = TypedChoiceField(choices=Choices(*range(1, 6)))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = helper.FormHelper(self)
        self.helper.form_id = 'entry-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        self.helper.html5_required = True
        self.helper.layout = layout.Layout(

            layout.Fieldset('Pubmed',

                            layout.Field('pubmed_id', autocomplete='off'),

                            layout.Div(

                                layout.Div(css_class=self.helper.label_class),

                                layout.Div(

                                    layout.HTML(

                                        '<p id=summary '
                                        'class=help-block></p>'

                                    ),

                                    css_class=self.helper.field_class

                                ),

                                css_class='form-group'

                            )

                            ),

            layout.Fieldset('Gene Description',

                            'gene', 'structure', 'mutation_type', 'syntax',
                            'syntax_text', 'operator', 'rule_level',

                            layout.Row(

                                layout.Column(

                                    Flat(

                                        'chromosome', 'start', 'stop',
                                        'breakend_strand', 'breakend_direction',

                                    ),

                                    css_class='col-sm-6',
                                    data_form_column='true'

                                ),

                                layout.HTML('<hr class="visible-xs">'),

                                layout.Column(

                                    Flat(

                                        'mate_chromosome', 'mate_start',
                                        'mate_end', 'mate_breakend_strand',
                                        'mate_breakend_direction',

                                    ),

                                    css_class='col-sm-6',
                                    data_form_column='true'

                                ),

                                css_class='well',

                            ),

                            layout.Row(

                                layout.Column(

                                    Flat('minimum_number_of_copies'),

                                    css_class='col-sm-6'

                                ),

                                layout.Column(

                                    Flat('maximum_number_of_copies'),

                                    css_class='col-sm-6',

                                ),

                                css_class='well well-sm'

                            ),

                            layout.Row(

                                layout.Column(

                                    Flat('coordinate_predicate'),

                                    css_class='col-sm-6'

                                ),

                                layout.Column(

                                    Flat('partner_coordinate_predicate'),

                                    css_class='col-sm-6',

                                ),

                                css_class='well well-sm'

                            ),

                            'variant_type', 'variant_consequence',
                            'variant_clinical_grade',

                            ),

            layout.Fieldset('Treatment',

                            'disease', 'treatment', 'treatment_1',
                            'treatment_2', 'treatment_3', 'treatment_4',
                            'treatment_5'

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

            layout.Div(css_id='results')

        )

        self.helper.filter_by_widget(forms.RadioSelect).wrap(
            bootstrap.InlineRadios)

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
