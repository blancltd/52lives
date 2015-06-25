# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0004_content_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liveblock',
            old_name='live',
            new_name='life',
        ),
        migrations.AlterField(
            model_name='life',
            name='number',
            field=models.PositiveIntegerField(blank=True, verbose_name='Life number', null=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='request',
            field=models.TextField(verbose_name='Life need'),
        ),
        migrations.AlterField(
            model_name='life',
            name='thank_you',
            field=models.TextField(blank=True, verbose_name='Thank you content form'),
        ),
    ]
