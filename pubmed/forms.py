"""
Pubmed forms.
"""

# Python Libraries
import logging

# Django Packages
from django.db import models
from django.forms import ModelForm, RadioSelect

# Third Party Packages
from braces import forms as braces_forms
from crispy_forms import bootstrap, helper
from model_utils import Choices

# Local Application
from .fields import TypedChoiceField
from .layouts import EntryFormLayout
from .lookups import BreakendDirectionLookup, BreakendStrandLookup, PatientOutcomesLookup
from .models import Entry, EntryMeta

logger = logging.getLogger(__name__)

models.BLANK_CHOICE_DASH[0] = ('', 'Null')


class EntryModelForm(braces_forms.UserKwargModelFormMixin, ModelForm):
    """
    Form representation of Pubmed Entry.

    :param args:
    :param kwargs:
    """
    # formfield_callback = entryform_formfield_callback
    # """Use radio inline widgets by default"""

    treatment = TypedChoiceField(choices=Choices(*range(1, 6)), required=False)
    """Helper field for dynamic treatment behavior."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in filter(lambda x: x not in ('user',), EntryMeta.foreign_fields):
            self.fields[field].empty_label = models.BLANK_CHOICE_DASH[0][1]

        breakend_strand = BreakendStrandLookup.objects.all()
        self.fields['breakend_strand'].queryset = breakend_strand
        self.fields['mate_breakend_strand'].queryset = breakend_strand

        breakend_direction = BreakendDirectionLookup.objects.all()
        self.fields['breakend_direction'].queryset = breakend_direction
        self.fields['mate_breakend_direction'].queryset = breakend_direction

        patient_outcomes = PatientOutcomesLookup.objects.all()
        self.fields['assessed_patient_outcomes'].queryset = patient_outcomes
        self.fields['significant_patient_outcomes'].queryset = patient_outcomes

        self.fields['pubmed_id'].help_text = ' '

        self.helper = helper.FormHelper(self)
        self.helper.form_id = 'entry-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        self.helper.html5_required = True
        self.helper.layout = EntryFormLayout(helper=self.helper)

        self.helper.filter_by_widget(RadioSelect).wrap(bootstrap.InlineRadios)

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
        fields = EntryMeta.public_fields
        widgets = {field: RadioSelect for field in EntryMeta.foreign_fields if not field == 'user'}
        widgets['treatment'] = RadioSelect
