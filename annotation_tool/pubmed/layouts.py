# Python Libraries
import logging

# Third Party Packages
from ..core.material.layouts import Submit, Button
from ..core.material.layouts import (HTML, Column, Div, Field, Fieldset, Layout, Row, ButtonGroup)

logger = logging.getLogger(__name__)


class EntryFormLayout(Layout):
    def __init__(self, helper, *args, **kwargs):
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

                             css_class='medium-6'

                         ),

                         HTML('<hr class="show-for-small-only">'),

                         Column(

                             'mate_chromosome', 'mate_start', 'mate_end', 'mate_breakend_strand',
                             'mate_breakend_direction',

                             css_class='medium-6'

                         ),

                         css_class='panel radius',

                     ),

                     Row(

                         Column(

                             'minimum_number_of_copies',

                             css_class='medium-6'

                         ),

                         Column(

                             'maximum_number_of_copies',

                             css_class='medium-6',

                         ),

                         css_class='panel radius'

                     ),

                     Row(

                         Column(

                             'coordinate_predicate',

                             css_class='medium-6'

                         ),

                         Column(

                             'partner_coordinate_predicate',

                             css_class='medium-6',

                         ),

                         css_class='panel radius'

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

                     ButtonGroup(Submit('submit', 'Submit'),
                                 Button('cancel', 'Cancel', css_class='secondary'),
                                 css_class='radius')

                     ),

            Div(css_id='results')

        )
