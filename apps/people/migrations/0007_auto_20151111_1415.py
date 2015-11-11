# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20151111_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
