# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_auto_20151109_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Address Line 2', blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_3',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Address Line 3', blank=True),
        ),
    ]
