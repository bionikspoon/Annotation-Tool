"""
Pubmed forms.
"""

# Python Libraries
import logging

# Django Packages
from django.db import models
from django.forms import ModelForm, RadioSelect, TypedChoiceField, HiddenInput, IntegerField

# Third Party Packages
from braces.forms import UserKwargModelFormMixin
from crispy_forms import helper
from model_utils import Choices

# Local Application
from .layouts import EntryFormLayout
from .lookups import (BreakendDirectionLookup, BreakendStrandLookup, MutationTypeLookup, OperatorLookup,
    PatientOutcomesLookup, RuleLevelLookup, SexLookup, StructureLookup, SyntaxLookup,
    VariantConsequenceLookup, VariantTypeLookup)
from .models import Entry, EntryMeta

logger = logging.getLogger(__name__)

models.BLANK_CHOICE_DASH[0] = ('', 'Null')


def model_choices(model):
    return ((lookup.pk, lookup.choice) for lookup in model.objects.only('choice'))


class EntryModelForm(UserKwargModelFormMixin, ModelForm):
    """
    Form representation of Pubmed Entry.

    :param args:
    :param kwargs:
    """
    # formfield_callback = entryform_formfield_callback
    # """Use radio inline widgets by default"""

    treatment = TypedChoiceField(choices=Choices(*range(1, 6)), required=False, widget=RadioSelect)
    """Helper field for dynamic treatment behavior."""
    id = IntegerField(widget=HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in filter(lambda x: x not in ('user',), EntryMeta.foreign_fields):
            self.fields[field].empty_label = models.BLANK_CHOICE_DASH[0][1]

        breakend_strand = tuple(model_choices(BreakendStrandLookup))
        self.fields['breakend_strand'].choices = breakend_strand
        self.fields['mate_breakend_strand'].choices = breakend_strand

        breakend_direction = tuple(model_choices(BreakendDirectionLookup))
        self.fields['breakend_direction'].choices = breakend_direction
        self.fields['mate_breakend_direction'].choices = breakend_direction

        patient_outcomes = tuple(model_choices(PatientOutcomesLookup))
        self.fields['assessed_patient_outcomes'].choices = patient_outcomes
        self.fields['significant_patient_outcomes'].choices = patient_outcomes

        self.fields['structure'].choices = model_choices(StructureLookup)
        self.fields['mutation_type'].choices = model_choices(MutationTypeLookup)
        self.fields['syntax'].choices = model_choices(SyntaxLookup)
        self.fields['operator'].choices = model_choices(OperatorLookup)
        self.fields['rule_level'].choices = model_choices(RuleLevelLookup)
        self.fields['variant_type'].choices = model_choices(VariantTypeLookup)
        self.fields['variant_consequence'].choices = model_choices(VariantConsequenceLookup)
        self.fields['sex'].choices = model_choices(SexLookup)

        self.fields['pubmed_id'].help_text = ' '

        self.helper = helper.FormHelper(self)
        self.helper.form_id = 'entry-form'
        self.helper.html5_required = True
        self.helper.layout = EntryFormLayout(helper=self.helper)

        # self.helper.filter_by_widget(RadioSelect).wrap(bootstrap.InlineRadios)

    def clean(self):
        """
        Remove unused treatment entries.

        :return:
        """
        cleaned_data = super().clean()
        treatment = int(cleaned_data.get('treatment') or 1)
        for i in range(treatment + 1, 6):
            cleaned_data['treatment_%s' % i] = ''

        return cleaned_data

    def save(self, commit=True):
        """
        Inject current user into model.

        :type commit: bool
        :return:
        """
        self.instance.user = self.user
        return super().save(commit)

    # noinspection PyDocstring
    class Meta:
        model = Entry
        fields = ('id',) + EntryMeta.public_fields
        widgets = {field: RadioSelect() for field in EntryMeta.foreign_fields if not field == 'user'}
