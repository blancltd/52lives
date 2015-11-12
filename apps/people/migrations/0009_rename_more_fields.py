# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_needs_as_textfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee',
            name='relation',
            field=models.CharField(max_length=124, verbose_name=b'How do you know the nominee?', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='home_phone',
            field=models.CharField(max_length=20, verbose_name=b'Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Please ensure you have the permission of those involved before sharing personal details, and familiarise yourself with our <a href="/terms/">terms and conditions</a> and <a href="/privacy/">data protection policy</a>.'),
        ),
    ]
