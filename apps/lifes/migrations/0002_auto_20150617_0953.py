# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
