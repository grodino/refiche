# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20150618_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'permissions': (('view_classroom', 'Peut voir la classe'),)},
        ),
        migrations.AlterModelOptions(
            name='sheet',
            options={},
        ),
    ]
