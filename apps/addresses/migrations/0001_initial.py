# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('type', models.IntegerField(default=1, choices=[(1, b'Primary')])),
                ('description', models.CharField(help_text=b'Description of address - Home, Office, Warehouse, etc.', max_length=20, null=True)),
                ('company_name', models.CharField(max_length=200, null=True, blank=True)),
                ('line_1', models.CharField(max_length=255)),
                ('line_2', models.CharField(max_length=255, null=True, blank=True)),
                ('line_3', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255, null=True, blank=True)),
                ('postcode', models.CharField(max_length=30)),
                ('default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
