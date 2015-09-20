# Python Libraries
import logging

# Django Packages

# Third Party Packages
from crispy_forms_foundation.layout import (HTML, Button, Column, Div, Field, Fieldset, Layout, Row,
    Submit, ButtonHolder)

logger = logging.getLogger(__name__)


# class Flat(LayoutObject):
#     template = "%s/layout/flat.html"
#
#     def __init__(self, *fields, **kwargs):
#         self.fields = list(fields)
#         self.css_class = kwargs.pop('css_class', '')
#         self.css_id = kwargs.pop('css_id', None)
#         self.template = kwargs.pop('template', self.template)
#         self.flat_attrs = flatatt(kwargs)
#
#     def get_rendered_fields(self, form, form_style, context, template_pack=TEMPLATE_PACK,
# **kwargs):
#         kwargs['template'] = 'flat/layout/field.html'
#         template_pack = 'flat'
#
#         def render(field):
#             return render_field(field, form, form_style, context, template_pack=template_pack,
# **kwargs)
#
#         return ''.join(render(field) for field in self.fields)
#
#     def render(self, form, form_style, context, template_pack, **kwargs):
#         template_pack = 'flat'
#         fields = self.get_rendered_fields(form, form_style, context, template_pack, **kwargs)
#         template = self.get_template_name(template_pack)
#         return render_to_string(template, {
#             'fieldset': self,
#             'fields': fields,
#             'form_style': form_style
#         })


class EntryFormLayout(Layout):
    def __init__(self, helper, *args, **kwargs):
        self.label_class = helper.label_class
        self.field_class = helper.field_class

        super().__init__(

            Field('id'),

            Fieldset('Pubmed',

                     Field('pubmed_id', autocomplete='off')

                     ),

            Fieldset('Gene Description',

                     'gene', 'structure', 'mutation_type', 'syntax', 'syntax_text', 'operator',
                     'rule_level',

                     Row(

                         Column(

                             'chromosome', 'start', 'stop', 'breakend_strand', 'breakend_direction',

                             css_class='col-sm-6', data_form_column='true'

                         ),

                         HTML('<hr class="visible-xs">'),

                         Column(

                             'mate_chromosome', 'mate_start', 'mate_end', 'mate_breakend_strand',
                             'mate_breakend_direction',

                             css_class='col-sm-6', data_form_column='true'

                         ),

                         css_class='well',

                     ),

                     Row(

                         Column(

                             'minimum_number_of_copies',

                             css_class='large-6'

                         ),

                         Column(

                             'maximum_number_of_copies',

                             css_class='large-6',

                         ),

                         css_class='well well-sm'

                     ),

                     Row(

                         Column(

                             'coordinate_predicate',

                             css_class='large-6'

                         ),

                         Column(

                             'partner_coordinate_predicate',

                             css_class='large-6',

                         ),

                         css_class='well well-sm'

                     ),

                     'variant_type', 'variant_consequence', 'variant_clinical_grade',

                     ),

            Fieldset('Treatment',

                     'disease', 'treatment', 'treatment_1', 'treatment_2', 'treatment_3',
                     'treatment_4', 'treatment_5'

                     ),

            Fieldset('Study',

                     'population_size', 'sex', 'ethnicity', 'assessed_patient_outcomes',
                     'significant_patient_outcomes', 'design', 'reference_claims', 'comments'

                     ),

            Fieldset('{{ action_text }} Entry',

                     ButtonHolder(Submit('submit', 'Submit'), Button('cancel', 'Cancel'))

                     ),

            Div(css_id='results')

        )
