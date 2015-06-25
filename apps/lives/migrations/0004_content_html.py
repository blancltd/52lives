# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.template.defaultfilters import linebreaksbr
from django.utils.html import linebreaks


def content_html(apps, schema_editor):
    Life = apps.get_model('lives', 'Life')

    for life in Life.objects.all():
        life.content = linebreaksbr(life.content)
        life.request = linebreaksbr(life.request)
        life.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0003_life_request_title'),
    ]

    operations = [
        migrations.RunPython(content_html, migrations.RunPython.noop)
    ]
