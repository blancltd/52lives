# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0007_latestlivesblock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestlivesblock',
            old_name='number_of_stories',
            new_name='number_of_lives',
        ),
    ]
