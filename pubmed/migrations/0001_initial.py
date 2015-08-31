# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pubmed_lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('pubmed_id', models.PositiveIntegerField()),
                ('gene', models.CharField(blank=True, max_length=100)),
                ('syntax_text', models.CharField(blank=True, max_length=100)),
                ('chromosome', models.CharField(blank=True, max_length=100)),
                ('start', models.PositiveIntegerField(blank=True, null=True)),
                ('stop', models.PositiveIntegerField(blank=True, null=True)),
                ('mate_chromosome', models.CharField(blank=True, max_length=100)),
                ('mate_start', models.PositiveIntegerField(blank=True, null=True)),
                ('mate_end', models.PositiveIntegerField(blank=True, null=True)),
                ('minimum_number_of_copies', models.PositiveIntegerField(blank=True, null=True)),
                ('maximum_number_of_copies', models.PositiveIntegerField(blank=True, null=True)),
                ('coordinate_predicate', models.CharField(blank=True, max_length=100)),
                ('partner_coordinate_predicate', models.CharField(blank=True, max_length=100)),
                ('variant_clinical_grade', models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('treatment_1', models.CharField(blank=True, max_length=100)),
                ('treatment_2', models.CharField(blank=True, max_length=100)),
                ('treatment_3', models.CharField(blank=True, max_length=100)),
                ('treatment_4', models.CharField(blank=True, max_length=100)),
                ('treatment_5', models.CharField(blank=True, max_length=100)),
                ('population_size', models.PositiveIntegerField(blank=True, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=100)),
                ('design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('assessed_patient_outcomes', models.ManyToManyField(blank=True, related_name='assessed_patient_outcomes', to='pubmed_lookup.PatientOutcomesLookup')),
                ('breakend_direction', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_direction', to='pubmed_lookup.BreakendDirectionLookup', null=True)),
                ('breakend_strand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakend_strand', to='pubmed_lookup.BreakendStrandLookup', null=True)),
                ('disease', models.ManyToManyField(blank=True, to='pubmed_lookup.DiseaseLookup')),
                ('mate_breakend_direction', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_direction', to='pubmed_lookup.BreakendDirectionLookup', null=True)),
                ('mate_breakend_strand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mate_breakend_strand', to='pubmed_lookup.BreakendStrandLookup', null=True)),
                ('mutation_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.MutationTypeLookup', null=True)),
                ('operator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.OperatorLookup', null=True)),
                ('rule_level', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.RuleLevelLookup', null=True)),
                ('sex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.SexLookup', null=True)),
                ('significant_patient_outcomes', models.ManyToManyField(blank=True, related_name='significant_patient_outcomes', to='pubmed_lookup.PatientOutcomesLookup')),
                ('structure', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.StructureLookup', null=True)),
                ('syntax', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.SyntaxLookup', null=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='pubmed_entries', to=settings.AUTH_USER_MODEL)),
                ('variant_consequence', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.VariantConsequenceLookup', null=True)),
                ('variant_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pubmed_lookup.VariantTypeLookup', null=True)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
