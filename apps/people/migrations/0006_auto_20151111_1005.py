# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_update_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('relation', models.CharField(max_length=124, verbose_name=b'How do you know nominee?', blank=True)),
                ('why_help', models.TextField(verbose_name=b'Why do they need help?', blank=True)),
                ('what_need', models.CharField(max_length=124, verbose_name=b'What do they need?', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Nominee',
            },
        ),
        migrations.CreateModel(
            name='Nominator',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='is_agreed',
            field=models.BooleanField(default=False, help_text=b'Please ensure you have the permission of those involved before sharing personal details, and familiarise yourself with our terms and conditions and data protection policy.'),
        ),
        migrations.AddField(
            model_name='nominee',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
    ]
