# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '__first__'),
        ('pages', '0005_auto_20150529_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('link_text', models.CharField(max_length=40, blank=True)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
                ('image', blanc_basic_assets.fields.AssetForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
            ],
            options={
                'ordering': ('link',),
            },
        ),
    ]
