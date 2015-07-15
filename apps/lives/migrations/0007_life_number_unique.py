# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0006_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name='Life number', unique=True, blank=True),
        ),
    ]
