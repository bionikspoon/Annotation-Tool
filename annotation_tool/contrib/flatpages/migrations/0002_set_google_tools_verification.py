# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from . import add_page, remove_page


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_page, remove_page)]
