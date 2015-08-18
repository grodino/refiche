# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150415_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='numberOfSheetsUploaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sheetFile',
            field=models.FileField(upload_to='sheets/'),
        ),
    ]
