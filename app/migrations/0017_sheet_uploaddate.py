# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_sheet_sheettype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='uploadDate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 20, 17, 17, 4, 466495, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
