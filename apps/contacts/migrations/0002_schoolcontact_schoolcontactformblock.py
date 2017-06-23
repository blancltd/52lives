# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.BLANC_PAGES_MODEL),
        ('pages', '0004_rename_tables'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('school', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=120, blank=True)),
                ('year_group', models.CharField(max_length=30, blank=True)),
                ('workshop_date', models.CharField(max_length=100, blank=True)),
                ('address', models.TextField(blank=True)),
                ('telephone', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=70)),
                ('confirm_email', models.EmailField(max_length=70)),
                ('hear_about', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'School contact form',
            },
        ),
        migrations.CreateModel(
            name='SchoolContactFormBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipient', models.EmailField(max_length=254)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
                ('success_page', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.BLANC_PAGES_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
