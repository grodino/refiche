# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_lesson_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='lessons',
            field=models.ManyToManyField(to='app.Lesson'),
        ),
        migrations.AddField(
            model_name='student',
            name='lessons',
            field=models.ManyToManyField(to='app.Lesson'),
        ),
    ]
