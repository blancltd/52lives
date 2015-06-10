# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150529_1016'),
        ('lifes', '0008_auto_20150610_1147'),
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
        migrations.RemoveField(
            model_name='latestlivesblock',
            name='content_block',
        ),
        migrations.AlterModelOptions(
            name='life',
            options={'ordering': ('-number',), 'get_latest_by': 'id'},
        ),
        migrations.DeleteModel(
            name='LatestLivesBlock',
        ),
    ]
