# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_change_hear_about_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Before submitting this form, please <a href="/privacy/">click here to read our privacy policy</a> and tick this box to confirm that you have read the policy notice and consent to the processing of your personal data and sensitive personal data.'),
        ),
    ]
