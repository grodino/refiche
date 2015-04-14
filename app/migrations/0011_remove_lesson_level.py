# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150408_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='level',
        ),
    ]
