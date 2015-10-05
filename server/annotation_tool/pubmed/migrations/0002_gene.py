# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('version', models.PositiveIntegerField()),
                ('hgnc_id', models.CharField(unique=True, db_index=True, max_length=16)),
                ('ccds_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=32))),
                ('cosmic', models.CharField(max_length=32)),
                ('date_modified', models.DateField()),
                ('date_approved_reserved', models.DateField()),
                ('name', models.CharField(max_length=32)),
                ('symbol', models.CharField(db_index=True, max_length=16)),
                ('alias_name', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=64))),
                ('alias_symbol', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('location', models.CharField(max_length=16)),
                ('location_sortable', models.CharField(max_length=16)),
                ('locus_type', models.CharField(max_length=32)),
                ('locus_group', models.CharField(max_length=32)),
                ('gene_family', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=64))),
                ('gene_family_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.PositiveIntegerField())),
                ('status', models.CharField(max_length=16)),
                ('entrez_id', models.PositiveIntegerField()),
                ('ensembl_gene_id', models.CharField(max_length=32)),
                ('refseq_accession', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('ena', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('pubmed_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.PositiveIntegerField())),
                ('rgd_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('snornabase', models.CharField(max_length=16)),
                ('ucsc_id', models.CharField(max_length=16)),
                ('uniprot_ids', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('vega_id', models.CharField(max_length=16)),
                ('mgd_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('omim_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.PositiveIntegerField())),
                ('enzyme_id', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
                ('horde_id', models.CharField(max_length=16)),
                ('lsdb', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=64))),
                ('bioparadigms_slc', models.CharField(max_length=16)),
                ('cd', models.CharField(max_length=16)),
                ('date_name_changed', models.DateField()),
                ('date_symbol_changed', models.DateField()),
                ('imgt', models.CharField(max_length=16)),
                ('intermediate_filament_db', models.CharField(max_length=16)),
                ('iuphar', models.CharField(max_length=16)),
                ('merops', models.CharField(max_length=16)),
                ('mirbase', models.CharField(max_length=16)),
                ('orphanet', models.CharField(max_length=16)),
                ('prev_name', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=64))),
                ('prev_symbol', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=16))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
