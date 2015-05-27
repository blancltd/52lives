# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0005_auto_20150521_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='life',
            options={'get_latest_by': 'id'},
        ),
    ]
