# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_3166_1_a2', models.CharField(help_text=b'http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=2, verbose_name=b'ISO 3166-1 alpha-2', blank=True)),
                ('iso_3166_1_a3', models.CharField(help_text=b'http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=3, verbose_name=b'ISO 3166-1 alpha-3', blank=True)),
                ('iso_3166_1_numeric', models.CharField(help_text=b'http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes', max_length=3, verbose_name=b'ISO 3166-1 numeric', blank=True)),
                ('name', models.CharField(help_text=b"The commonly used name; e.g. 'United Kingdom'", max_length=128, verbose_name=b'Country name')),
                ('display_order', models.PositiveSmallIntegerField(default=0, help_text=b'Higher the number, higher the country in the list.', verbose_name=b'Display order', db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
