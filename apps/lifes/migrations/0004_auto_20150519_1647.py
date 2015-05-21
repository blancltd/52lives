# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0003_auto_20150519_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'Is accepted?'),
        ),
    ]
