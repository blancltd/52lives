# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='description',
            field=models.CharField(help_text='Description of address - Home, Office, Warehouse, etc.', null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.IntegerField(choices=[(1, 'Primary')], default=1),
        ),
    ]
