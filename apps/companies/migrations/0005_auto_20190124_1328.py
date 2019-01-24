# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20160527_1143'),
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
            field=sorl.thumbnail.fields.ImageField(verbose_name='Profile image', upload_to='uploads/companies/life/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='is_published',
            field=models.BooleanField(verbose_name='Is accepted?', default=False),
        ),
        migrations.AlterField(
            model_name='life',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Life number', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='request',
            field=models.TextField(verbose_name='Life need'),
        ),
        migrations.AlterField(
            model_name='life',
            name='summary',
            field=models.TextField(verbose_name='What we did', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='thank_you',
            field=models.TextField(verbose_name='Thank you content form', blank=True),
        ),
        migrations.AlterField(
            model_name='life',
            name='title',
            field=models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Sir', 'Sir')], blank=True),
        ),
    ]
