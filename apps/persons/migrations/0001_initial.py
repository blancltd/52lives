# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0001_initial'),
        migrations.swappable_dependency(settings.BLANC_PAGES_MODEL),
        ('pages', '0004_rename_tables'),
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
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10, choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs'), (b'Ms', 'Ms'), (b'Miss', 'Miss'), (b'Dr', 'Dr'), (b'Sir', 'Sir')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('home_phone', models.CharField(max_length=20, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, blank=True)),
                ('reason', models.IntegerField(choices=[(1, b'I would like to nominate someone'), (2, b'I can help'), (3, b'Something else')])),
                ('message', models.TextField()),
                ('hear_about_us', models.CharField(max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('live', models.ForeignKey(blank=True, to='lives.Live', null=True)),
            ],
        ),
    ]
