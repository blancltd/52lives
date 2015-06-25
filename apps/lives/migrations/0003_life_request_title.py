# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0002_auto_20150625_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='life',
            name='request_title',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
