# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20150618_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'permissions': (('can_add', 'peut ajouter une lesson'),)},
        ),
    ]
