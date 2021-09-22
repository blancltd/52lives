# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '__first__'),
        ('pages', '0004_rename_tables'),
        ('lives52_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoColumnBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column_one_title', models.TextField()),
                ('column_one_video_embed_link', models.URLField(blank=True)),
                ('column_one_colour', models.CharField(blank=True, max_length=40, choices=[(b'dark_purple', b'Dark Purple'), (b'purple', b'Purple'), (b'green', b'Green')])),
                ('column_two_title', models.TextField()),
                ('column_two_video_embed_link', models.URLField(blank=True)),
                ('column_two_colour', models.CharField(blank=True, max_length=40, choices=[(b'dark_purple', b'Dark Purple'), (b'purple', b'Purple'), (b'green', b'Green')])),
                ('column_ratio', models.CharField(blank=True, max_length=40, choices=[(b'even', b'1:1'), (b'stack-right', b'1:2'), (b'stack-left', b'2:1')])),
                ('column_one_thumbnail_image', blanc_basic_assets.fields.AssetForeignKey(related_name='first_image', on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
                ('column_two_thumbnail_image', blanc_basic_assets.fields.AssetForeignKey(related_name='second_image', on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
