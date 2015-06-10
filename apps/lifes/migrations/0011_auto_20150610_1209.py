# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifes', '0010_lifeblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeblock',
            name='life',
            field=models.ForeignKey(blank=True, to='lifes.Life', null=True),
        ),
    ]
