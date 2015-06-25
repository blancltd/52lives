# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='content',
            field=models.TextField(verbose_name='Content about live'),
        ),
        migrations.AlterField(
            model_name='life',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='uploads/lives/live/%Y/%m/%d', verbose_name='Profile image', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='is_published',
            field=models.BooleanField(verbose_name='Is accepted?', default=False),
        ),
        migrations.AlterField(
            model_name='life',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Live number', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='request',
            field=models.TextField(verbose_name='Live need'),
        ),
        migrations.AlterField(
            model_name='life',
            name='summary',
            field=models.TextField(verbose_name='What we did', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='thank_you',
            field=models.TextField(verbose_name='Thank you content form live', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Sir', 'Sir')], blank=True, max_length=10),
        ),
    ]
