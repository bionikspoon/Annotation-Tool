# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges
import model_utils.fields
import django.core.validators
from django.conf import settings
import django.contrib.postgres.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('version', models.BigIntegerField()),
                ('hgnc_id', models.CharField(max_length=16, db_index=True, unique=True)),
                ('ccds_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), size=None)),
                ('cosmic', models.CharField(max_length=32)),
                ('date_modified', models.DateTimeField()),
                ('date_approved_reserved', models.DateTimeField()),
                ('name', models.CharField(max_length=32)),
                ('symbol', models.CharField(max_length=16, db_index=True)),
                ('alias_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None)),
                ('alias_symbol', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('location', models.CharField(max_length=16)),
                ('location_sortable', models.CharField(max_length=16)),
                ('locus_type', models.CharField(max_length=32)),
                ('locus_group', models.CharField(max_length=32)),
                ('gene_family', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('gene_family_id', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None)),
                ('status', models.CharField(max_length=16)),
                ('entrez_id', models.BigIntegerField()),
                ('ensembl_gene_id', models.CharField(max_length=32)),
                ('refseq_accession', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None)),
                ('ena', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('pubmed_id', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), null=True, size=None)),
                ('rgd_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('snornabase', models.CharField(max_length=16, null=True)),
                ('ucsc_id', models.CharField(max_length=16, null=True)),
                ('uniprot_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('vega_id', models.CharField(max_length=16, null=True)),
                ('mgd_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('omim_id', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), null=True, size=None)),
                ('enzyme_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
                ('homeodb', models.BigIntegerField(null=True)),
                ('horde_id', models.CharField(max_length=16, null=True)),
                ('lsdb', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None)),
                ('kznf_gene_catalog', models.BigIntegerField(null=True)),
                ('lncrnadb', models.BigIntegerField(null=True)),
                ('bioparadigms_slc', models.CharField(max_length=16, null=True)),
                ('cd', models.CharField(max_length=16, null=True)),
                ('date_name_changed', models.DateTimeField(null=True)),
                ('date_symbol_changed', models.DateTimeField(null=True)),
                ('imgt', models.CharField(max_length=16, null=True)),
                ('intermediate_filament_db', models.CharField(max_length=16, null=True)),
                ('iuphar', models.CharField(max_length=16, null=True)),
                ('merops', models.CharField(max_length=16, null=True)),
                ('mirbase', models.CharField(max_length=16, null=True)),
                ('orphanet', models.CharField(max_length=16, null=True)),
                ('prev_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None)),
                ('prev_symbol', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), null=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientOutcomesLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pubmed',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pubmed_id', models.PositiveIntegerField(db_index=True)),
                ('gene', models.CharField(max_length=128, blank=True)),
                ('syntax_text', models.CharField(max_length=128, blank=True)),
                ('operator', models.CharField(max_length=32, choices=[('CONTAINS', 'Contains'), ('NOT CONTAINS', 'Not Contains')], blank=True)),
                ('chromosome', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(23)], choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)], blank=True)),
                ('chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('breakend_strand', models.CharField(max_length=32, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], blank=True)),
                ('breakend_direction', models.CharField(max_length=32, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], blank=True)),
                ('mate_chromosome', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(23)], choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)], blank=True)),
                ('mate_chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('mate_breakend_strand', models.CharField(max_length=32, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')], blank=True)),
                ('mate_breakend_direction', models.CharField(max_length=32, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], blank=True)),
                ('number_of_copies', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('partner_coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('variant_clinical_grade', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5)], choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True)),
                ('treatment_number_of_arms', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5)], choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True)),
                ('population_size', models.PositiveIntegerField(null=True, blank=True)),
                ('sex', models.CharField(max_length=32, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('MIXED', 'Mixed'), ('UNKNOWN', 'Unknown')], blank=True)),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('study_design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('assessed_patient_outcomes', models.ManyToManyField(related_name='assessed_patient_outcomes_pubmed_entries', to='pubmed.PatientOutcomesLookup', blank=True)),
                ('disease', models.ManyToManyField(related_name='pubmed_entries', to='pubmed.DiseaseLookup', blank=True)),
                ('mutation_type', models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.MutationTypeLookup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('choice', models.CharField(max_length=128, db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pubmed',
            name='rule_level',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.RuleLevelLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(related_name='significant_patient_outcomes_pubmed_entries', to='pubmed.PatientOutcomesLookup', blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='structure',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.StructureLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.SyntaxLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(related_name='pubmed_entries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_consequence',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.VariantConsequenceLookup'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(null=True, related_name='pubmed_entries', to='pubmed.VariantTypeLookup'),
        ),
    ]
