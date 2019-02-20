# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150625_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='frequently_used',
            field=models.BooleanField(default=False, help_text=b'Tick this box if you want the country to display at the top of the list of available countries.'),
        ),
    ]
