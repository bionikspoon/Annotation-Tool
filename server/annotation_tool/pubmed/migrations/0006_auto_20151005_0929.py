# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0005_auto_20151005_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='alias_name',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=64)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='alias_symbol',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='bioparadigms_slc',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='cd',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_name_changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='date_symbol_changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ena',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='enzyme_id',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='homeodb',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='horde_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='imgt',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='intermediate_filament_db',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='iuphar',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='kznf_gene_catalog',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='lncrnadb',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='lsdb',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=64)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='merops',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='mgd_id',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='mirbase',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='omim_id',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.BigIntegerField()),
        ),
        migrations.AlterField(
            model_name='gene',
            name='orphanet',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='prev_name',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=64)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='prev_symbol',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='pubmed_id',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.BigIntegerField()),
        ),
        migrations.AlterField(
            model_name='gene',
            name='rgd_id',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='snornabase',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ucsc_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='uniprot_ids',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=16)),
        ),
        migrations.AlterField(
            model_name='gene',
            name='vega_id',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
