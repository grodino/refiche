# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.functions


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20150606_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='chapter',
            field=models.ForeignKey(null=True, to='app.Chapter', verbose_name='chapitre'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='lesson',
            field=models.ForeignKey(to='app.Lesson', verbose_name='matière'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sheetFile',
            field=models.FileField(upload_to=app.functions.renameFile, verbose_name='fichier'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sheetType',
            field=models.CharField(default='SHEET', choices=[('SHEET', 'fiche'), ('NOTES', 'cours'), ('TEST', 'sujetDeContrôle'), ('TEST_CORRECTION', 'corrigéDeContrôle')], max_length=50, verbose_name='catégorie'),
        ),
    ]
