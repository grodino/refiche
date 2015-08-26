# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150406_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(default=1, to='app.School'),
            preserve_default=False,
        ),
    ]
