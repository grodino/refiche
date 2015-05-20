# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20150520_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(max_length=4, choices=[('M.', 'Monsieur'), ('Mme', 'Madame'), ('Mlle', 'Mademoiselle')]),
        ),
    ]
