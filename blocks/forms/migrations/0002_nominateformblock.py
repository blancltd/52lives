# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.BLANC_PAGES_MODEL),
        ('pages', '0005_auto_20150529_1016'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NominateFormBlock',
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
