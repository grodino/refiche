# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20150520_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='extension',
            field=models.CharField(max_length=50, default='.test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sheet',
            name='contentType',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sheetType',
            field=models.CharField(max_length=50, default='SHEET', choices=[('SHEET', 'fiche'), ('NOTES', 'cours'), ('TEST', 'sujetDeContrôle'), ('TEST_CORRECTION', 'corrigéDeContrôle')]),
        ),
    ]
