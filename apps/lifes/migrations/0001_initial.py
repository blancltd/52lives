# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150529_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestLifesBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_lives', models.PositiveIntegerField(default=10)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
            ],
            options={
                'verbose_name': 'Latest lifes',
            },
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10, choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs'), (b'Ms', 'Ms'), (b'Miss', 'Miss'), (b'Dr', 'Dr'), (b'Sir', 'Sir')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.PositiveIntegerField(null=True, verbose_name=b'Life number', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/lifes/life/%Y/%m/%d', verbose_name=b'Profile image', blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('home_phone', models.CharField(max_length=20, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, blank=True)),
                ('content', models.TextField(verbose_name=b'Content about life')),
                ('request', models.TextField(verbose_name=b'Life need')),
                ('summary', models.TextField(verbose_name=b'What we did', blank=True)),
                ('thank_you', models.TextField(verbose_name=b'Thank you content form life', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'Is accepted?')),
                ('slug', models.SlugField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-number',),
                'get_latest_by': 'id',
            },
        ),
        migrations.CreateModel(
            name='LifeBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
                ('life', models.ForeignKey(blank=True, to='lifes.Life', null=True)),
            ],
            options={
                'verbose_name': 'Life',
            },
        ),
    ]
