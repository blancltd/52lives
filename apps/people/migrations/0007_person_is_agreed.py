# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20151109_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Please ensure you have the permission of those involved before sharing personal details, and familiarise yourself with our terms and conditions and data protection policy.'),
        ),
    ]
