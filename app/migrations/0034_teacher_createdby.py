# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20150619_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='createdBy',
            field=models.ForeignKey(default=30, to='app.Student'),
            preserve_default=False,
        ),
    ]
