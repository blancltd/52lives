# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_address_verbose_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(verbose_name='Address Line 1', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(verbose_name='Address Line 2', max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_3',
            field=models.CharField(verbose_name='Address Line 3', max_length=255, blank=True, null=True),
        ),
    ]
