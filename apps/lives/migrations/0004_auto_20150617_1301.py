# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0003_auto_20150617_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
