# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_sheet_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='chapter',
            field=models.ForeignKey(to='app.Chapter', null=True),
        ),
    ]
