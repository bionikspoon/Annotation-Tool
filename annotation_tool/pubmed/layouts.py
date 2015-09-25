# Python Libraries
import logging
# Third Party Packages
from crispy_forms.layout import (Layout, Field, Fieldset, Row, Div, Button, Column)

from ..bootstrap.layout import Column6, Submit, Cancel

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

                         Column6(

                             'chromosome', 'start', 'stop', 'breakend_strand', 'breakend_direction',

                             css_class='mdl-cell mdl-cell--6-col'

                         ),

                         # HTML('<hr class="show-for-small-only">'),

                         Column6(

                             'mate_chromosome', 'mate_start', 'mate_end', 'mate_breakend_strand',
                             'mate_breakend_direction',

                             css_class='mdl-cell mdl-cell--6-col'

                         ),

                         css_class='well well-sm mdl-grid'

                     ),

                     Row(

                         Column(

                             'minimum_number_of_copies',

                             css_class='mdl-cell mdl-cell--6-col'

                         ),

                         Column(

                             'maximum_number_of_copies',

                             css_class='mdl-cell mdl-cell--6-col',

                         ),

                         css_class='well well-sm mdl-grid'

                     ),

                     Row(

                         Column(

                             'coordinate_predicate',

                             css_class='mdl-cell mdl-cell--6-col'

                         ),

                         Column(

                             'partner_coordinate_predicate',

                             css_class='mdl-cell mdl-cell--6-col',

                         ),

                         css_class='well well-sm mdl-grid'

                     ),

                     'variant_type', 'variant_consequence', 'variant_clinical_grade',

                     ),

            Fieldset('Treatment',

                     'disease', 'treatment', 'treatment_1', 'treatment_2', 'treatment_3',
                     'treatment_4', 'treatment_5',

                     ),

            Fieldset('Study',

                     'population_size', 'sex', 'ethnicity', 'assessed_patient_outcomes',
                     'significant_patient_outcomes', 'design', 'reference_claims', 'comments',

                     ),

            Fieldset('{{ action_text }} Entry',

                     Submit('submit', '{{ action_text }}'),

                     Cancel('cancel', 'Cancel')

                     ),

        )
