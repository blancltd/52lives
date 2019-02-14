# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_change_is_agreed_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolcontact',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Before submitting this form, please\n           <a href="/privacy/">click here to read our privacy policy</a>\n           and tick this box to confirm that you have read the policy notice and consent to the \n           processing of your personal data and sensitive personal data.'),
        ),
        migrations.AlterField(
            model_name='schoolcontact',
            name='workshop_date',
            field=models.TextField(blank=True),
        ),
    ]
