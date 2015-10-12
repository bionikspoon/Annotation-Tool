# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_auto_20151012_2240'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gene',
        ),
        migrations.DeleteModel(
            name='GeneAliasNameLookup',
        ),
        migrations.DeleteModel(
            name='GeneAliasSymbolLookup',
        ),
        migrations.DeleteModel(
            name='GeneCdsIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneEnaLookup',
        ),
        migrations.DeleteModel(
            name='GeneEnzymeIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneGeneFamilyIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneGeneFamilyLookup',
        ),
        migrations.DeleteModel(
            name='GeneLsdbLookup',
        ),
        migrations.DeleteModel(
            name='GeneMgdIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneOmimIdLookup',
        ),
        migrations.DeleteModel(
            name='GenePrevNameLookup',
        ),
        migrations.DeleteModel(
            name='GenePrevSymbolLookup',
        ),
        migrations.DeleteModel(
            name='GenePubmedIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneRefseqAccessionLookup',
        ),
        migrations.DeleteModel(
            name='GeneRgdIdLookup',
        ),
        migrations.DeleteModel(
            name='GeneUniprotIdsLookup',
        ),
    ]
