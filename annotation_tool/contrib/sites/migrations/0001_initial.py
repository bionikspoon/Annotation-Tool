# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.sites.models


class Migration(migrations.Migration):


    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('domain', models.CharField(validators=[django.contrib.sites.models._simple_domain_name_validator], verbose_name='domain name', max_length=100)),
                ('name', models.CharField(verbose_name='display name', max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'verbose_name_plural': 'sites',
                'verbose_name': 'site',
                'ordering': ('domain',),
            },
            managers=[
                (b'objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='site',
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
