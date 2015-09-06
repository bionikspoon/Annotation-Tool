# Compatibility
from __future__ import unicode_literals

# Django Packages
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

# Third Party Packages
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [('lookups', '0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL), ]

    operations = [migrations.CreateModel(

        name='Entry',

        fields=[

            ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),

            ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                            verbose_name='created')),

            ('modified',
             model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                      verbose_name='modified')),
            ('pubmed_id', models.PositiveIntegerField()),

            ('gene', models.CharField(blank=True, max_length=100)),
            ('syntax_text', models.CharField(blank=True, max_length=100)),
            ('chromosome', models.CharField(blank=True, max_length=100)),
            ('start', models.PositiveIntegerField(null=True, blank=True)),
            ('stop', models.PositiveIntegerField(null=True, blank=True)),
            ('mate_chromosome', models.CharField(blank=True, max_length=100)),
            ('mate_start', models.PositiveIntegerField(null=True, blank=True)),
            ('mate_end', models.PositiveIntegerField(null=True, blank=True)),
            ('minimum_number_of_copies', models.PositiveIntegerField(null=True, blank=True)),
            ('maximum_number_of_copies', models.PositiveIntegerField(null=True, blank=True)),
            ('coordinate_predicate', models.CharField(blank=True, max_length=100)),
            ('partner_coordinate_predicate', models.CharField(blank=True, max_length=100)),

            ('variant_clinical_grade', models.PositiveIntegerField(

                null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),

            ('treatment_1', models.CharField(blank=True, max_length=100)),
            ('treatment_2', models.CharField(blank=True, max_length=100)),
            ('treatment_3', models.CharField(blank=True, max_length=100)),
            ('treatment_4', models.CharField(blank=True, max_length=100)),
            ('treatment_5', models.CharField(blank=True, max_length=100)),
            ('population_size', models.PositiveIntegerField(null=True, blank=True)),
            ('ethnicity', models.CharField(blank=True, max_length=100)),

            ('design', models.TextField(blank=True)),

            ('reference_claims', models.TextField(blank=True)),

            ('comments', models.TextField(blank=True)),

            ('assessed_patient_outcomes',
             models.ManyToManyField(to='lookups.PatientOutcomesLookup', blank=True,
                                    related_name='assessed_patient_outcomes_entry_set')),

            ('breakend_direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                     to='lookups.BreakendDirectionLookup', blank=True,
                                                     related_name='breakend_direction_entry_set')),

            ('breakend_strand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                  to='lookups.BreakendStrandLookup', blank=True,
                                                  related_name='breakend_strand_entry_set')),
            ('disease', models.ManyToManyField(to='lookups.DiseaseLookup', blank=True)),

            ('mate_breakend_direction',
             models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                               to='lookups.BreakendDirectionLookup', blank=True,
                               related_name='mate_breakend_direction_entry_set')),

            ('mate_breakend_strand',
             models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                               to='lookups.BreakendStrandLookup', blank=True,
                               related_name='mate_breakend_strand_entry_set')),

            ('mutation_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                to='lookups.MutationTypeLookup', blank=True)),

            ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='lookups.OperatorLookup', blank=True)),

            ('rule_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to='lookups.RuleLevelLookup', blank=True)),

            ('sex', models.ForeignKey(

                null=True, on_delete=django.db.models.deletion.SET_NULL, to='lookups.SexLookup', blank=True)),

            ('significant_patient_outcomes', models.ManyToManyField(

                to='lookups.PatientOutcomesLookup', blank=True,
                related_name='significant_patient_outcomes_entry_set')),

            ('structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                            to='lookups.StructureLookup', blank=True)),

            ('syntax', models.ForeignKey(

                null=True, on_delete=django.db.models.deletion.SET_NULL, to='lookups.SyntaxLookup',
                blank=True)),

            ('user',
             models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL,
                               editable=False, related_name='pubmed_entries')),

            ('variant_consequence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                      to='lookups.VariantConsequenceLookup', blank=True)),

            ('variant_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='lookups.VariantTypeLookup', blank=True))

        ],

        options={
            'verbose_name_plural': 'Entries'
        }

    )]
