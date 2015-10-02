# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pubmed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pubmed_id', models.PositiveIntegerField(db_index=True)),
                ('gene', models.CharField(blank=True, max_length=128)),
                ('chromosome', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
