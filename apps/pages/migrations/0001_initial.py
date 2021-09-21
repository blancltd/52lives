# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '__first__'),
        ('pages', '0004_rename_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('video_embed_link', models.URLField(blank=True)),
                ('colour', models.CharField(blank=True, max_length=40, choices=[(b'dark_purple', b'Dark Purple'), (b'purple', b'Purple'), (b'green', b'Green')])),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
                ('thumbnail_image', blanc_basic_assets.fields.AssetForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
