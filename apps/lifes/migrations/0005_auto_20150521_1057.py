# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0004_auto_20150519_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='life',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='life',
            name='home_phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='life',
            name='mobile_phone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
