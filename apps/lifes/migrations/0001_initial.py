# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10, choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs'), (b'Ms', 'Ms'), (b'Miss', 'Miss'), (b'Dr', 'Dr'), (b'Sir', 'Sir')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.PositiveIntegerField(null=True, verbose_name=b'Life number', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/lifes/life/%Y/%m/%d', verbose_name=b'Profile image', blank=True)),
                ('content', models.TextField(verbose_name=b'Content about life')),
                ('request', models.TextField(verbose_name=b'Life need')),
                ('summary', models.TextField(verbose_name=b'What we did', blank=True)),
                ('thank_you', models.TextField(verbose_name=b'Thank you content form life', blank=True)),
                ('is_publish', models.BooleanField(default=False, verbose_name=b'Accept? Life number will be assign')),
                ('slug', models.SlugField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
