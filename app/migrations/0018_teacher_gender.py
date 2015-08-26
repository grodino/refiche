# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_sheet_uploaddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('MR', 'Monsieur'), ('MRS', 'Madame'), ('MISS', 'Mademoiselle')], max_length=4, default='MR'),
            preserve_default=False,
        ),
    ]
