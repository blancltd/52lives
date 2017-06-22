# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_remove_life_life_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Life number', blank=True),
        ),
        migrations.AlterModelOptions(
            name='life',
            options={'ordering': ('number',), 'verbose_name_plural': 'Lives'},
        ),
        migrations.AlterUniqueTogether(
            name='life',
            unique_together=set([('company', 'number')]),
        ),
    ]
