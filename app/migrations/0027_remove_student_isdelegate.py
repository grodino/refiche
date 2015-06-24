# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20150614_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='isDelegate',
        ),
    ]
