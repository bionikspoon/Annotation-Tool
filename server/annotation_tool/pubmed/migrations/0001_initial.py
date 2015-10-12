# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import django.utils.timezone
import django.contrib.postgres.fields.ranges
import django.core.validators
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('hgnc_id', models.CharField(max_length=128, db_index=True, unique=True)),
                ('ccds_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('cosmic', models.CharField(max_length=128)),
                ('date_modified', models.DateTimeField(null=True)),
                ('date_approved_reserved', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=256)),
                ('symbol', models.CharField(max_length=128, db_index=True)),
                ('alias_name', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('alias_symbol', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('location', models.CharField(max_length=128)),
                ('location_sortable', models.CharField(max_length=128)),
                ('locus_type', models.CharField(max_length=128)),
                ('locus_group', models.CharField(max_length=128)),
                ('gene_family', django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(null=True, max_length=128))),
                ('gene_family_id', django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.BigIntegerField(null=True))),
                ('status', models.CharField(max_length=128)),
                ('entrez_id', models.BigIntegerField(null=True)),
                ('ensembl_gene_id', models.CharField(max_length=128)),
                ('refseq_accession', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('ena', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('pubmed_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.BigIntegerField())),
                ('rgd_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('snornabase', models.CharField(null=True, max_length=128)),
                ('ucsc_id', models.CharField(null=True, max_length=128)),
                ('uniprot_ids', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('vega_id', models.CharField(null=True, max_length=128)),
                ('mgd_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('omim_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.BigIntegerField())),
                ('enzyme_id', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('homeodb', models.BigIntegerField(null=True)),
                ('horde_id', models.CharField(null=True, max_length=128)),
                ('lsdb', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('kznf_gene_catalog', models.BigIntegerField(null=True)),
                ('lncrnadb', models.CharField(null=True, max_length=32)),
                ('bioparadigms_slc', models.CharField(null=True, max_length=128)),
                ('cd', models.CharField(null=True, max_length=128)),
                ('date_name_changed', models.DateTimeField(null=True)),
                ('date_symbol_changed', models.DateTimeField(null=True)),
                ('imgt', models.CharField(null=True, max_length=128)),
                ('intermediate_filament_db', models.CharField(null=True, max_length=128)),
                ('iuphar', models.CharField(null=True, max_length=128)),
                ('merops', models.CharField(null=True, max_length=128)),
                ('mirbase', models.CharField(null=True, max_length=128)),
                ('orphanet', models.CharField(null=True, max_length=128)),
                ('prev_name', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
                ('prev_symbol', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pubmed_id', models.PositiveIntegerField(db_index=True)),
                ('gene', models.CharField(max_length=128, blank=True)),
                ('syntax_text', models.CharField(max_length=128, blank=True)),
                ('operator', models.CharField(max_length=32, blank=True, choices=[('CONTAINS', 'Contains'), ('NOT CONTAINS', 'Not Contains')])),
                ('chromosome', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(23)], null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('breakend_strand', models.CharField(max_length=32, blank=True, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')])),
                ('breakend_direction', models.CharField(max_length=32, blank=True, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')])),
                ('mate_chromosome', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(23)], null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('mate_chromosome_range', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('mate_breakend_strand', models.CharField(max_length=32, blank=True, choices=[('FORWARD', 'Forward'), ('REVERSE', 'Reverse')])),
                ('mate_breakend_direction', models.CharField(max_length=32, blank=True, choices=[('LEFT', 'Left'), ('RIGHT', 'Right')])),
                ('number_of_copies', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True, blank=True)),
                ('coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('partner_coordinate_predicate', models.CharField(max_length=32, blank=True)),
                ('variant_clinical_grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('treatment_number_of_arms', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('population_size', models.PositiveIntegerField(null=True, blank=True)),
                ('sex', models.CharField(max_length=32, blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('MIXED', 'Mixed'), ('UNKNOWN', 'Unknown')])),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('study_design', models.TextField(blank=True)),
                ('reference_claims', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('assessed_patient_outcomes', models.ManyToManyField(to='pubmed.PatientOutcomesLookup', related_name='assessed_patient_outcomes_pubmed_entries', blank=True)),
                ('disease', models.ManyToManyField(to='pubmed.DiseaseLookup', related_name='pubmed_entries', blank=True)),
                ('mutation_type', models.ForeignKey(null=True, to='pubmed.MutationTypeLookup', related_name='pubmed_entries')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ForeignKey(null=True, to='pubmed.RuleLevelLookup', related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.PatientOutcomesLookup', related_name='significant_patient_outcomes_pubmed_entries', blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='structure',
            field=models.ForeignKey(null=True, to='pubmed.StructureLookup', related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax',
            field=models.ForeignKey(null=True, to='pubmed.SyntaxLookup', related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_consequence',
            field=models.ForeignKey(null=True, to='pubmed.VariantConsequenceLookup', related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(null=True, to='pubmed.VariantTypeLookup', related_name='pubmed_entries'),
        ),
    ]
