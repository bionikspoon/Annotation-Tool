# Compatibility
from __future__ import unicode_literals

# Django Packages
from django.db import migrations

# Local Application
from . import add_page, remove_page


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_page, remove_page)]
