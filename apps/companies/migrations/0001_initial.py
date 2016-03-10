# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='uploads/companies/company/%Y/%m/%d', blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=10, choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs'), (b'Ms', 'Ms'), (b'Miss', 'Miss'), (b'Dr', 'Dr'), (b'Sir', 'Sir')])),
                ('first_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('number', models.PositiveIntegerField(unique=True, null=True, verbose_name=b'Life number', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='uploads/companies/life/%Y/%m/%d', verbose_name=b'Profile image', blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('home_phone', models.CharField(max_length=20, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, blank=True)),
                ('request_title', models.CharField(max_length=100)),
                ('content', models.TextField(verbose_name=b'Content about live')),
                ('request', models.TextField(verbose_name=b'Life need')),
                ('summary', models.TextField(verbose_name=b'What we did', blank=True)),
                ('thank_you', models.TextField(verbose_name=b'Thank you content form', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'Is accepted?')),
                ('slug', models.SlugField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
        ),
    ]
