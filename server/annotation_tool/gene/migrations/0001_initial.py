# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import server.annotation_tool.utils.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AliasNameLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AliasSymbolLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CcdsIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EnaLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EnzymeIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('version', models.BigIntegerField()),
                ('hgnc_id', models.CharField(db_index=True, max_length=128, unique=True)),
                ('cosmic', models.CharField(max_length=128)),
                ('date_modified', models.DateTimeField(null=True)),
                ('date_approved_reserved', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=256)),
                ('symbol', models.CharField(db_index=True, max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('location_sortable', models.CharField(max_length=128)),
                ('locus_type', models.CharField(max_length=128)),
                ('locus_group', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('entrez_id', models.BigIntegerField(null=True)),
                ('ensembl_gene_id', models.CharField(max_length=128)),
                ('snornabase', models.CharField(null=True, max_length=128)),
                ('ucsc_id', models.CharField(null=True, max_length=128)),
                ('vega_id', models.CharField(null=True, max_length=128)),
                ('homeodb', models.BigIntegerField(null=True)),
                ('horde_id', models.CharField(null=True, max_length=128)),
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
                ('alias_name', models.ManyToManyField(to='gene.AliasNameLookup', blank=True)),
                ('alias_symbol', models.ManyToManyField(to='gene.AliasSymbolLookup', blank=True)),
                ('ccds_id', models.ManyToManyField(to='gene.CcdsIdLookup', blank=True)),
                ('ena', models.ManyToManyField(to='gene.EnaLookup', blank=True)),
                ('enzyme_id', models.ManyToManyField(to='gene.EnzymeIdLookup', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneFamilyIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.PositiveIntegerField(db_index=True, unique=True)),
            ],
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GeneFamilyLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LsdbLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MgdIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OmimIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PrevNameLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=256, unique=True)),
            ],
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PrevSymbolLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PubmedIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RefseqAccessionLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RgdIdLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UniprotIdsLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(server.annotation_tool.utils.models.LookupMixin, models.Model),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene_family',
            field=models.ManyToManyField(to='gene.GeneFamilyLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene_family_id',
            field=models.ManyToManyField(to='gene.GeneFamilyIdLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='lsdb',
            field=models.ManyToManyField(to='gene.LsdbLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='mgd_id',
            field=models.ManyToManyField(to='gene.MgdIdLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='omim_id',
            field=models.ManyToManyField(to='gene.OmimIdLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='prev_name',
            field=models.ManyToManyField(to='gene.PrevNameLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='prev_symbol',
            field=models.ManyToManyField(to='gene.PrevSymbolLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='pubmed_id',
            field=models.ManyToManyField(to='gene.PubmedIdLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='refseq_accession',
            field=models.ManyToManyField(to='gene.RefseqAccessionLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='rgd_id',
            field=models.ManyToManyField(to='gene.RgdIdLookup', blank=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='uniprot_ids',
            field=models.ManyToManyField(to='gene.UniprotIdsLookup', blank=True),
        ),
    ]
