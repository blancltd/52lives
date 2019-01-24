# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150625_1118'),
        ('people', '0009_rename_more_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='phone',
        ),
        migrations.AddField(
            model_name='nominee',
            name='country',
            field=models.ForeignKey(blank=True, to='countries.Country', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Before submitting your nomination, please <a href="https://52lives.contentfiles.net/media/assets/file/Final_Privacy_Notice_Nominator_Q0KzKUJ.pdf">click here to read our privacy notice</a> and tick this box to confirm that you have read the policy notice and consent to the processing of your personal data and sensitive personal data.'),
        ),
    ]
