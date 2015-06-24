# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20150606_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='lesson',
            field=models.ForeignKey(to='app.Lesson', default=1),
            preserve_default=False,
        ),
    ]
