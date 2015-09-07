"""
Pubmed model definitions.
"""

# Python Libraries
from collections import OrderedDict

# Django Packages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Third Party Packages
from model_utils import models as utils_models
from model_utils import Choices

# Annotation Tool Project
from annotation_tool.users.models import User

# Local Application
from . import lookups
from .utils import classproperty


class DEFAULTS(object):
    """
    Default parameters for given key.
    """
    CharField = dict(max_length=100, blank=True)
    ForeignKey = dict(blank=True, null=True, on_delete=models.SET_NULL)
    IntegerField = dict(null=True, blank=True)
    TextField = dict(blank=True)
    ManyToManyField = dict(blank=True)


class Entry(utils_models.TimeStampedModel):
    """
    Pubmed Entry definition.
    """
    user = models.ForeignKey(

        settings.AUTH_USER_MODEL, editable=False, related_name='pubmed_entries', on_delete=models.PROTECT

    )
    pubmed_id = models.PositiveIntegerField()
    gene = models.CharField(**DEFAULTS.CharField)
    structure = models.ForeignKey(lookups.StructureLookup, **DEFAULTS.ForeignKey)
    mutation_type = models.ForeignKey(lookups.MutationTypeLookup, **DEFAULTS.ForeignKey)
    syntax = models.ForeignKey(lookups.SyntaxLookup, **DEFAULTS.ForeignKey)
    syntax_text = models.CharField(**DEFAULTS.CharField)
    operator = models.ForeignKey(lookups.OperatorLookup, **DEFAULTS.ForeignKey)
    rule_level = models.ForeignKey(lookups.RuleLevelLookup, **DEFAULTS.ForeignKey)
    chromosome = models.CharField(**DEFAULTS.CharField)
    start = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    stop = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    breakend_strand = models.ForeignKey(

        lookups.BreakendStrandLookup, related_name='breakend_strand_entry_set', **DEFAULTS.ForeignKey

    )
    breakend_direction = models.ForeignKey(

        lookups.BreakendDirectionLookup, related_name='breakend_direction_entry_set', **DEFAULTS.ForeignKey

    )
    mate_chromosome = models.CharField(**DEFAULTS.CharField)
    mate_start = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    mate_end = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    mate_breakend_strand = models.ForeignKey(

        lookups.BreakendStrandLookup, related_name='mate_breakend_strand_entry_set', **DEFAULTS.ForeignKey

    )
    mate_breakend_direction = models.ForeignKey(

        lookups.BreakendDirectionLookup, related_name='mate_breakend_direction_entry_set',
        **DEFAULTS.ForeignKey

    )
    minimum_number_of_copies = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    maximum_number_of_copies = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    coordinate_predicate = models.CharField(**DEFAULTS.CharField)
    partner_coordinate_predicate = models.CharField(**DEFAULTS.CharField)
    variant_type = models.ForeignKey(lookups.VariantTypeLookup, **DEFAULTS.ForeignKey)
    variant_consequence = models.ForeignKey(lookups.VariantConsequenceLookup, **DEFAULTS.ForeignKey)
    variant_clinical_grade = models.PositiveIntegerField(

        choices=Choices(*range(1, 6)), **DEFAULTS.IntegerField

    )
    disease = models.ManyToManyField(lookups.DiseaseLookup, **DEFAULTS.ManyToManyField)
    treatment_1 = models.CharField(**DEFAULTS.CharField)
    treatment_2 = models.CharField(**DEFAULTS.CharField)
    treatment_3 = models.CharField(**DEFAULTS.CharField)
    treatment_4 = models.CharField(**DEFAULTS.CharField)
    treatment_5 = models.CharField(**DEFAULTS.CharField)
    population_size = models.PositiveIntegerField(**DEFAULTS.IntegerField)
    sex = models.ForeignKey(lookups.SexLookup, **DEFAULTS.ForeignKey)
    ethnicity = models.CharField(**DEFAULTS.CharField)
    assessed_patient_outcomes = models.ManyToManyField(

        lookups.PatientOutcomesLookup, related_name='assessed_patient_outcomes_entry_set',
        **DEFAULTS.ManyToManyField

    )
    significant_patient_outcomes = models.ManyToManyField(

        lookups.PatientOutcomesLookup, related_name='significant_patient_outcomes_entry_set',
        **DEFAULTS.ManyToManyField

    )
    design = models.TextField(**DEFAULTS.TextField)
    reference_claims = models.TextField(**DEFAULTS.TextField)
    comments = models.TextField(**DEFAULTS.TextField)

    # tracker = FieldTracker()

    def get_absolute_url(self):
        """
        Link to entry.

        :return: URL path.
        """
        kwargs = {
            'pk': self.id
        }
        return reverse('pubmed:detail', kwargs=kwargs)

    def __str__(self):
        gene = ':%s' % self.gene if self.gene else ''
        return '%s:%s%s' % (self.pubmed_id, self.id, gene)

    class Meta:
        verbose_name_plural = 'Entries'


# noinspection PyMethodParameters
class EntryMeta(object):
    """
    Describe pubmed entry class.
    """
    model = Entry

    fields_manifest = OrderedDict([

        ('id', {
            'public': False,
            'field_type': 'AutoField',
            'summary': False
        }),

        ('created', {
            'public': False,
            'field_type': 'AutoCreatedField',
            'summary': False
        }),

        ('modified', {
            'public': False,
            'field_type': 'AutoLastModifiedField',
            'summary': True
        }),

        ('user', {
            'public': False,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('pubmed_id', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('gene', {
            'public': True,
            'field_type': 'CharField',
            'summary': True
        }),

        ('structure', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('mutation_type', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('syntax', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('syntax_text', {
            'public': True,
            'field_type': 'CharField',
            'summary': True
        }),

        ('operator', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('rule_level', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': True
        }),

        ('chromosome', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('start', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('stop', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('breakend_strand', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('breakend_direction', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('mate_chromosome', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('mate_start', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('mate_end', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('mate_breakend_strand', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('mate_breakend_direction', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('minimum_number_of_copies', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('maximum_number_of_copies', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('coordinate_predicate', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('partner_coordinate_predicate', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('variant_type', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('variant_consequence', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('variant_clinical_grade', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('disease', {
            'public': True,
            'field_type': 'ManyToManyField',
            'summary': False
        }),

        ('treatment_1', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('treatment_2', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('treatment_3', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('treatment_4', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('treatment_5', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('population_size', {
            'public': True,
            'field_type': 'PositiveIntegerField',
            'summary': False
        }),

        ('sex', {
            'public': True,
            'field_type': 'ForeignKey',
            'summary': False
        }),

        ('ethnicity', {
            'public': True,
            'field_type': 'CharField',
            'summary': False
        }),

        ('assessed_patient_outcomes', {
            'public': True,
            'field_type': 'ManyToManyField',
            'summary': False
        }),

        ('significant_patient_outcomes', {
            'public': True,
            'field_type': 'ManyToManyField',
            'summary': False
        }),

        ('design', {
            'public': True,
            'field_type': 'TextField',
            'summary': False
        }),

        ('reference_claims', {
            'public': True,
            'field_type': 'TextField',
            'summary': False
        }),

        ('comments', {
            'public': True,
            'field_type': 'TextField',
            'summary': False
        }),

    ])
    """List of fields of pubmed entry fields with meta data for grouping."""

    @classmethod
    def filter(cls, term):
        """
        Get fields with matching properties.

        :param cls:
        :type cls: EntryMeta
        :param term: Key-Value dictionary to filter by.
        :type term: dict | tuple
        :return: A tuple of fields that survive the filter.
        :rtype : tuple(str)
        """

        key, value = tuple((k, v) for k, v in term.items())[0]

        try:

            return tuple(

                field

                for field, meta in cls.fields_manifest.items()

                if meta.get(key) is value or meta.get(key) in value

            )
        except TypeError:

            return tuple(

                field

                for field, meta in cls.fields_manifest.items()

                if meta.get(key) is value

            )

    @classproperty
    def all_fields(cls):
        """
        Get all fields.

        :param cls: Entry
        :return:
        """

        return tuple(field for field, _ in cls.fields_manifest.items())

    @classproperty
    def relationship_fields(cls):
        """
        Get many to many fields and foreign key fields.

        :param cls: Entry
        :return:
        """

        return cls.filter({
            'field_type': ('ForeignKey', 'ManyToManyField')
        })

    @classproperty
    def foreign_fields(cls):
        """
        Get foreign key fields.

        :param cls:
        :return:
        """

        return cls.filter({
            'field_type': 'ForeignKey'
        })

    @classproperty
    def many_to_many_fields(cls):
        """
        Get many to many fields.

        :param cls:
        :return:
        """

        return cls.filter({
            'field_type': 'ManyToManyField'
        })

    @classproperty
    def text_fields(cls):
        """
        Get all text entry fields.

        :param cls:
        :return:
        """
        return cls.filter({
            'field_type': ('CharField', 'TextField')
        })

    @classproperty
    def int_fields(cls):
        """
        Get all integer fields.

        :param cls:
        :return:
        """

        return cls.filter({
            'field_type': 'PositiveIntegerField'
        })

    @classproperty
    def public_fields(cls):
        """
        Get fields to show on admin pages and forms.

        :param cls:
        :return:
        """
        return cls.filter({
            'public': True
        })

    @classproperty
    def summary_fields(cls):
        """
        Get fields to show on summary page and admin list pages.
        :param cls:
        :return:
        """
        return cls.filter({
            'summary': True
        })
