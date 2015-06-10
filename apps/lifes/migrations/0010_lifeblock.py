# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150529_1016'),
        ('lifes', '0009_auto_20150610_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_block', models.ForeignKey(editable=False, to='pages.ContentBlock', null=True)),
                ('life', models.ForeignKey(to='lifes.Life')),
            ],
            options={
                'verbose_name': 'Life',
            },
        ),
    ]
