# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150406_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='likeMaths',
        ),
        migrations.AddField(
            model_name='student',
            name='isDelegate',
            field=models.BooleanField(default=False),
        ),
    ]
