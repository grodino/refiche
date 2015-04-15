# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_sheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='uploadedBy',
            field=models.ForeignKey(to='app.Student'),
        ),
    ]
