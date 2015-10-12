# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('version', models.BigIntegerField()),
                ('hgnc_id', models.CharField(max_length=128, db_index=True, unique=True)),
                ('cosmic', models.CharField(max_length=128)),
                ('date_modified', models.DateTimeField(null=True)),
                ('date_approved_reserved', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=256)),
                ('symbol', models.CharField(max_length=128, db_index=True)),
                ('location', models.CharField(max_length=128)),
                ('location_sortable', models.CharField(max_length=128)),
                ('locus_type', models.CharField(max_length=128)),
                ('locus_group', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('entrez_id', models.BigIntegerField(null=True)),
                ('ensembl_gene_id', models.CharField(max_length=128)),
                ('snornabase', models.CharField(max_length=128, null=True)),
                ('ucsc_id', models.CharField(max_length=128, null=True)),
                ('vega_id', models.CharField(max_length=128, null=True)),
                ('homeodb', models.BigIntegerField(null=True)),
                ('horde_id', models.CharField(max_length=128, null=True)),
                ('kznf_gene_catalog', models.BigIntegerField(null=True)),
                ('lncrnadb', models.CharField(max_length=32, null=True)),
                ('bioparadigms_slc', models.CharField(max_length=128, null=True)),
                ('cd', models.CharField(max_length=128, null=True)),
                ('date_name_changed', models.DateTimeField(null=True)),
                ('date_symbol_changed', models.DateTimeField(null=True)),
                ('imgt', models.CharField(max_length=128, null=True)),
                ('intermediate_filament_db', models.CharField(max_length=128, null=True)),
                ('iuphar', models.CharField(max_length=128, null=True)),
                ('merops', models.CharField(max_length=128, null=True)),
                ('mirbase', models.CharField(max_length=128, null=True)),
                ('orphanet', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
