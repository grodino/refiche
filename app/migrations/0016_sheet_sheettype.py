# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_sheet_contenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='sheetType',
            field=models.CharField(default='SHEET', max_length=50, choices=[('SHEET', 'Fiche'), ('NOTES', 'Cours'), ('TEST', 'Sujet de contrôle'), ('TEST_CORRECTION', 'Corrigé de contrôle')]),
        ),
    ]
