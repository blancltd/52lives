# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0002_auto_20150519_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='life',
            old_name='is_publish',
            new_name='is_published',
        ),
    ]
