# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20151111_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee',
            name='what_need',
            field=models.TextField(verbose_name=b'What do they need?', blank=True),
        ),
    ]
