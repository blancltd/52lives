# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150625_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='hear_about_us',
            field=models.CharField(max_length=120, verbose_name=b'How did you hear about us?'),
        ),
    ]
