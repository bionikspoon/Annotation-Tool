from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import django.utils.timezone
import django.contrib.postgres.fields.ranges
from django.conf import settings
import django.core.validators
import annotation_tool.core.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [

        migrations.CreateModel(
            name='DiseaseLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='MutationTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='PatientOutcomesLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='Pubmed',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
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
                ('mutation_type', models.ForeignKey(related_name='pubmed_entries', to='pubmed.MutationTypeLookup', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='RuleLevelLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='StructureLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='SyntaxLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='VariantConsequenceLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),

        migrations.CreateModel(
            name='VariantTypeLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=128, unique=True, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(annotation_tool.core.utils.model_utils.LookupMixin, models.Model),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='rule_level',
            field=models.ForeignKey(related_name='pubmed_entries', to='pubmed.RuleLevelLookup', null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='significant_patient_outcomes',
            field=models.ManyToManyField(to='pubmed.PatientOutcomesLookup', related_name='significant_patient_outcomes_pubmed_entries', blank=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='structure',
            field=models.ForeignKey(related_name='pubmed_entries', to='pubmed.StructureLookup', null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='syntax',
            field=models.ForeignKey(related_name='pubmed_entries', to='pubmed.SyntaxLookup', null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pubmed_entries'),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_consequence',
            field=models.ForeignKey(related_name='pubmed_entries', to='pubmed.VariantConsequenceLookup', null=True),
        ),
        migrations.AddField(
            model_name='pubmed',
            name='variant_type',
            field=models.ForeignKey(related_name='pubmed_entries', to='pubmed.VariantTypeLookup', null=True),
        ),
    ]
