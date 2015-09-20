from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [('sites', '0002_set_site_domain_and_name'), ]

    dependencies = [
        ('sites', '0002_set_site_domain_and_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url', models.CharField(verbose_name='URL', max_length=100, db_index=True)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('enable_comments', models.BooleanField(verbose_name='enable comments', default=False)),
                ('template_name', models.CharField(verbose_name='template name', max_length=70, blank=True, help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.")),
                ('registration_required', models.BooleanField(verbose_name='registration required', default=False, help_text='If this is checked, only logged-in users will be able to view the page.')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'flat page',
                'ordering': ('url',),
                'db_table': 'django_flatpage',
                'verbose_name_plural': 'flat pages',
            },
        ),
    ]
