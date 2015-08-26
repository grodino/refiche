# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20150430_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='contentType',
            field=models.CharField(max_length=50, default='application/application'),
            preserve_default=False,
        ),
    ]
