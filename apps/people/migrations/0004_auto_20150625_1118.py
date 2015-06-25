# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20150617_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='reason',
            field=models.IntegerField(choices=[(1, 'I would like to nominate someone'), (2, 'I can help'), (3, 'Something else')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Sir', 'Sir')], max_length=10),
        ),
    ]
