# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liveblock',
            options={'verbose_name': 'Live'},
        ),
        migrations.AlterField(
            model_name='live',
            name='content',
            field=models.TextField(verbose_name=b'Content about live'),
        ),
        migrations.AlterField(
            model_name='live',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'uploads/lives/live/%Y/%m/%d', verbose_name=b'Profile image', blank=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Live number', blank=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='request',
            field=models.TextField(verbose_name=b'Live need'),
        ),
        migrations.AlterField(
            model_name='live',
            name='thank_you',
            field=models.TextField(verbose_name=b'Thank you content form live', blank=True),
        ),
    ]
