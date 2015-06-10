# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150529_1016'),
        ('lifes', '0006_auto_20150527_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestLivesBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_stories', models.PositiveIntegerField(default=10)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
            ],
            options={
                'verbose_name': 'Latest lives',
            },
        ),
    ]
