# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0002_auto_20150617_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='nominee',
            field=models.CharField(default='jau', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='live',
            name='first_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='last_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='title',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs'), (b'Ms', 'Ms'), (b'Miss', 'Miss'), (b'Dr', 'Dr'), (b'Sir', 'Sir')]),
        ),
    ]
