# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.BLANC_PAGES_MODEL),
        ('pages', '0004_rename_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, blank=True)),
                ('email', models.EmailField(max_length=70)),
                ('subject', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFormBlock',
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
