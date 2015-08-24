# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='breakend_direction',
            field=models.ForeignKey(to='pubmed.BreakendDirectionLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='breakend_strand',
            field=models.ForeignKey(to='pubmed.BreakendStrandLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='mate_breakend_strand',
            field=models.ForeignKey(to='pubmed.MateBreakendStrandLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='mutation_type',
            field=models.ForeignKey(to='pubmed.MutationTypeLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='operator',
            field=models.ForeignKey(to='pubmed.OperatorLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='rule_level',
            field=models.ForeignKey(to='pubmed.RuleLevelLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='sex',
            field=models.ForeignKey(to='pubmed.SexLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='structure',
            field=models.ForeignKey(to='pubmed.StructureLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='syntax',
            field=models.ForeignKey(to='pubmed.SyntaxLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_consequence',
            field=models.ForeignKey(to='pubmed.VariantConsequenceLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='variant_type',
            field=models.ForeignKey(to='pubmed.VariantTypeLookup', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True),
        ),
    ]
