# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20150615_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sheet',
            options={'permissions': (('view_sheet', 'Peut voir la fiche'),)},
        ),
    ]
