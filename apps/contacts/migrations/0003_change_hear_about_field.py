# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_schoolcontact_schoolcontactformblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolcontact',
            name='hear_about',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
