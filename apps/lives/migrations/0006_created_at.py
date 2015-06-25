# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0005_live_life'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
