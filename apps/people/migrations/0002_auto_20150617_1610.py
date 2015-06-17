# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominateformblock',
            name='content_block',
        ),
        migrations.RemoveField(
            model_name='nominateformblock',
            name='success_page',
        ),
        migrations.DeleteModel(
            name='NominateFormBlock',
        ),
    ]
