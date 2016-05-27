# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_life_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='life',
            name='life_number',
        ),
    ]
