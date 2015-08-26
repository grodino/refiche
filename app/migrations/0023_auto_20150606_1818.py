# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='lesson',
        ),
        migrations.AddField(
            model_name='chapter',
            name='lesson',
            field=models.ForeignKey(default=1, to='app.Lesson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='chapter',
            field=models.ForeignKey(default=1, to='app.Chapter'),
            preserve_default=False,
        ),
    ]
