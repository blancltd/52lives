# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='display_order',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='Display order', help_text='Higher the number, higher the country in the list.', default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso_3166_1_a2',
            field=models.CharField(verbose_name='ISO 3166-1 alpha-2', blank=True, help_text='http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=2),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso_3166_1_a3',
            field=models.CharField(verbose_name='ISO 3166-1 alpha-3', blank=True, help_text='http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=3),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso_3166_1_numeric',
            field=models.CharField(verbose_name='ISO 3166-1 numeric', blank=True, help_text='http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=3),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(verbose_name='Country name', help_text="The commonly used name; e.g. 'United Kingdom'", max_length=128),
        ),
    ]
