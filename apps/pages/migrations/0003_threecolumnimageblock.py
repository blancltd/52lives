# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '__first__'),
        ('pages', '0004_rename_tables'),
        ('lives52_pages', '0002_twocolumnblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeColumnImageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column_one_heading', models.TextField()),
                ('column_two_heading', models.TextField()),
                ('column_three_heading', models.TextField()),
                ('column_one_image', blanc_basic_assets.fields.AssetForeignKey(related_name='first_column_image', on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
                ('column_three_image', blanc_basic_assets.fields.AssetForeignKey(related_name='third_column_image', on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
                ('column_two_image', blanc_basic_assets.fields.AssetForeignKey(related_name='second_column_image', on_delete=django.db.models.deletion.PROTECT, blank=True, to='assets.Image', null=True)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
